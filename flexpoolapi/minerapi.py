#
#   Software distrubuted under MIT License (MIT)
#
#   Copyright (c) 2020 Flexpool
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of
#  the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
#  THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import requests
import datetime

from . import exceptions
from . import shared
from . import utils
from . import workerapi

__MINER_API_ENDPOINT__ = None


def update_endpoint(endpoint):
    global __MINER_API_ENDPOINT__
    __MINER_API_ENDPOINT__ = endpoint + "/miner"


class Transaction:
    def __init__(self, amount: int, timestamp: int, duration: int, txid: str):
        self.amount = amount
        self.time = datetime.datetime.fromtimestamp(timestamp)
        self.duration = duration
        self.txid = txid

    def __repr__(self):
        return "<flexpoolapi.miner.Transaction object " \
               f" {utils.format_weis(self.amount)} ({self.time.strftime('%Y %b %d %H:%M')})>"


class MinerDetails:
    def __init__(self, address: str, min_payout_threshold: int, pool_donation: int, censored_email: str,
                 censored_ip: str, first_joined_timestamp: int):
        self.address = address
        self.min_payout_threshold = min_payout_threshold
        self.pool_donation = pool_donation
        self.censored_email = censored_email
        self.censored_ip = censored_ip
        self.first_joined_date = datetime.datetime.fromtimestamp(
            first_joined_timestamp)

    def __repr__(self):
        return "<flexpoolapi.miner.MinerDetails object "\
            f"({self.address})>"


class MinerAPI:
    def __init__(self, address: str):
        self.endpoint = __MINER_API_ENDPOINT__ + f"/{address}"
        self.address = address

        try:
            tmp = address
            if address[:2] == "0x":
                tmp = tmp[2:]
            int(tmp, 16)
            if len(tmp) != 40:
                raise(ValueError())
        except ValueError:
            raise(exceptions.InvalidMinerAddress(
                f"Address {address} is invalid!"))

        api_request = requests.get(self.endpoint + "/exists")
        shared.check_response(api_request)

        if not api_request.json()["result"]:
            raise(exceptions.MinerDoesNotExist(
                f"Miner {address} does not exist"))

    def balance(self):
        api_request = requests.get(self.endpoint + "/balance")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def current_hashrate(self):
        api_request = requests.get(self.endpoint + "/current")
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        return api_request["effective_hashrate"], api_request["reported_hashrate"]

    def stats(self):
        api_request = requests.get(self.endpoint + "/stats")
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        class_ = shared.Stats(
            api_request["current"]["effective_hashrate"], api_request["daily"]["effective_hashrate"],
            api_request["current"]["reported_hashrate"], api_request["daily"]["reported_hashrate"],
            api_request["daily"]["valid_shares"], api_request["daily"]["stale_shares"],
            api_request["daily"]["invalid_shares"])
        return class_

    def daily_average_stats(self):
        api_request = requests.get(self.endpoint + "/daily")
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        class_ = shared.DailyAverageStats(
            api_request["effective_hashrate"], api_request["reported_hashrate"],
            api_request["valid_shares"], api_request["stale_shares"], api_request["invalid_shares"])

        return class_

    def worker_count(self):
        api_request = requests.get(self.endpoint + "/workerCount")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def workers(self):
        api_request = requests.get(self.endpoint + "/workers")
        shared.check_response(api_request)
        classed_workers = []
        for worker_ in api_request.json()["result"]:
            classed_workers.append(
                workerapi.Worker(self.address, worker_["name"], worker_["online"], worker_["last_seen"]))

        return classed_workers

    def chart(self):
        api_request = requests.get(self.endpoint + "/chart")
        shared.check_response(api_request)
        items = []
        for item in api_request.json()["result"]:
            items.append(shared.StatChartItem(
                item["effective_hashrate"], item["reported_hashrate"],
                item["valid_shares"], item["stale_shares"], item["invalid_shares"],
                item["timestamp"]
            ))
        return items

    def payments_paged(self, page):
        api_request = requests.get(
            self.endpoint + "/payments", params=[("page", page)])
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        classed_payments = []
        for raw_tx in api_request["data"]:
            classed_payments.append(Transaction(
                raw_tx["amount"], raw_tx["timestamp"], raw_tx["duration"], raw_tx["txid"]))

        return shared.PageResponse(
            classed_payments, api_request["total_items"], api_request["total_pages"], api_request["items_per_page"])

    def payment_count(self):
        api_request = requests.get(self.endpoint + "/paymentCount")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def blocks_paged(self, page):
        api_request = requests.get(
            self.endpoint + "/blocks", params=[("page", page)])
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        classed_blocks = []
        for raw_block in api_request["data"]:
            classed_blocks.append(shared.Block(
                raw_block["number"], raw_block["hash"], raw_block["type"], raw_block["miner"], raw_block["difficulty"],
                raw_block["timestamp"], raw_block["confirmed"], raw_block["round_time"], raw_block["luck"],
                raw_block["server_name"], raw_block["block_reward"], raw_block["block_fees"],
                raw_block["uncle_inclusion_rewards"], raw_block["total_rewards"]))
        return shared.PageResponse(
            classed_blocks, api_request["total_items"], api_request["total_pages"], api_request["items_per_page"])

    def block_count(self):
        api_request = requests.get(self.endpoint + "/blockCount")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def details(self):
        api_request = requests.get(self.endpoint + "/details")
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        return MinerDetails(self.address, api_request["min_payout_threshold"], api_request["pool_donation"],
                            api_request["censored_email"], api_request["censored_ip"], api_request["first_joined"])

    def estimated_daily_profit(self):
        api_request = requests.get(self.endpoint + "/estimatedDailyProfit")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def total_paid(self):
        api_request = requests.get(self.endpoint + "/totalPaid")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def total_donated(self):
        api_request = requests.get(self.endpoint + "/totalDonated")
        shared.check_response(api_request)
        return api_request.json()["result"]

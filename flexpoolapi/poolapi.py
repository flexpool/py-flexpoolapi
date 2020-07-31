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

from . import shared
from . import utils

__POOL_API_ENDPOINT__ = None


def update_endpoint(endpoint):
    global __POOL_API_ENDPOINT__
    __POOL_API_ENDPOINT__ = endpoint + "/pool"


class HashrateChartItem:
    def __init__(self, servers_hashrate: {str: int}, total_hashrate: int, timestamp: int):
        self.servers = servers_hashrate
        self.total_hashrate = total_hashrate
        self.timestamp = timestamp

    def __repr__(self):
        servers = []
        for server_name, server_hashrate in self.servers.items():
            servers.append(
                f"{server_name} ({utils.format_hashrate(server_hashrate)})")

        return "<flexpoolapi.pool.HashrateChartItem object " + ", ".join(servers) + ">"


class TopMiner:
    def __init__(self,
                 address: str, hashrate: int, pool_donation: float, balance: int, total_workers: int, first_joined_timestamp: int):
        self.address = address
        self.hashrate = hashrate
        self.pool_donation = pool_donation
        self.balance = balance
        self.total_workers = total_workers
        self.first_joined = datetime.datetime.fromtimestamp(
            first_joined_timestamp)

    def __repr__(self):
        return f"<flexpoolapi.pool.TopMiner object {self.address}: {utils.format_hashrate(self.hashrate)}>"


class TopDonator:
    def __init__(self,
                 address: str, total_donated: int, pool_donation: float, hashrate: int, first_joined_timestamp: int):
        self.address = address
        self.total_donated = total_donated
        self.pool_donation = pool_donation
        self.hashrate = hashrate
        self.first_joined = datetime.datetime.fromtimestamp(
            first_joined_timestamp)

    def __repr__(self):
        return f"<flexpoolapi.pool.TopDonator object {self.address}: {utils.format_weis(self.total_donated)}>"


class PoolAPI:
    def __init__(self):
        self.endpoint = __POOL_API_ENDPOINT__

    def hashrate(self):
        api_request = requests.get(self.endpoint + "/hashrate")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def hashrate_chart(self):
        api_request = requests.get(self.endpoint + "/hashrateChart")
        shared.check_response(api_request)
        hashrate_chart_classed = []
        for item in api_request.json()["result"]:
            total_hashrate = item["total"]
            timestamp = item["timestamp"]
            del item["total"], item["timestamp"]
            hashrate_chart_classed.append(
                HashrateChartItem(item, total_hashrate, timestamp))
        return hashrate_chart_classed

    def miners_online(self):
        api_request = requests.get(self.endpoint + "/minersOnline")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def workers_online(self):
        api_request = requests.get(self.endpoint + "/workersOnline")
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

    def last_blocks(self, count=10):
        blocks = shared.get_last_items_from_paged_response(
            self.endpoint + "/blocks", items_count=count)
        classed_blocks = []
        for raw_block in blocks:
            classed_blocks.append(shared.Block(
                raw_block["number"], raw_block["hash"], raw_block["type"], raw_block["miner"], raw_block["difficulty"],
                raw_block["timestamp"], raw_block["confirmed"], raw_block["round_time"], raw_block["luck"],
                raw_block["server_name"], raw_block["block_reward"], raw_block["block_fees"],
                raw_block["uncle_inclusion_rewards"], raw_block["total_rewards"]))
        return classed_blocks

    def block_count(self):
        api_request = requests.get(self.endpoint + "/blockCount")
        shared.check_response(api_request)
        return api_request.json()["result"]

    def top_miners(self):
        api_request = requests.get(self.endpoint + "/topMiners")
        shared.check_response(api_request)
        top_miners_classed = []
        for top_miner in api_request.json()["result"]:
            top_miners_classed.append(
                TopMiner(
                    top_miner["address"],
                    top_miner["hashrate"],
                    top_miner["pool_donation"],
                    top_miner["balance"],
                    top_miner["total_workers"],
                    top_miner["first_joined"]
                )
            )
        return top_miners_classed

    def top_donators(self):
        api_request = requests.get(self.endpoint + "/topDonators")
        shared.check_response(api_request)
        top_donators_classed = []
        for top_donator in api_request.json()["result"]:
            top_donators_classed.append(
                TopDonator(
                    top_donator["address"],
                    top_donator["total_donated"],
                    top_donator["pool_donation"],
                    top_donator["hashrate"],
                    top_donator["first_joined"]
                )
            )

        return top_donators_classed

    def avg_luck_roundtime(self) -> (float, float):
        api_request = requests.get(self.endpoint + "/avgLuckRoundtime")
        shared.check_response(api_request)
        api_request = api_request.json()["result"]
        return api_request["luck"], round(api_request["round_time"], 2)

    def current_luck(self) -> (float):
        api_request = requests.get(self.endpoint + "/currentLuck")
        shared.check_response(api_request)
        return api_request.json()["result"]

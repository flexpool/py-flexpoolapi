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

__WORKER_API_ENDPOINT__ = None


def update_endpoint(endpoint):
    global __WORKER_API_ENDPOINT__
    __WORKER_API_ENDPOINT__ = endpoint + "/worker"


class Worker:
    def __init__(self, address: str, worker_name: str, online: bool, last_seen_timestamp: int):
        # Warning: this class is expected to be initialized only by this library itself.
        # There are no checks either the given address + worker_name exist or not.
        self.address = address
        self.worker_name = worker_name
        self.is_online = online
        self.last_seen_date = datetime.datetime.fromtimestamp(
            last_seen_timestamp)

        self.endpoint = __WORKER_API_ENDPOINT__ + \
            f"/{self.address}/{self.worker_name}"

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

    def __repr__(self):
        return "<flexpoolapi.worker.Worker object "\
            f"{self.worker_name} ({self.address})>"

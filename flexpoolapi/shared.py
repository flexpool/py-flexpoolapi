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
from . import utils


class DailyAverageStats:
    def __init__(self, effective: int, reported: int, valid: int, stale: int, invalid: int):
        self.effective_hashrate = effective
        self.reported_hashrate = reported
        self.valid_shares = valid
        self.stale_shares = stale
        self.invalid_shares = invalid

    def __repr__(self):
        return f"<flexpoolapi.shared.DailyAverageStats object {utils.format_hashrate(self.effective_hashrate)}>"


class Stats:
    def __init__(self, effective: int, effective_day: int, reported: int, reported_day: int,
                 valid: int, stale: int, invalid: int):
        self.current_effective_hashrate = effective
        self.current_reported_hashrate = reported

        self.average_effective_hashrate = effective_day
        self.average_reported_hashrate = reported_day

        self.valid_shares = valid
        self.stale_shares = stale
        self.invalid_shares = invalid

    def __repr__(self):
        return f"<flexpoolapi.shared.Stats object {utils.format_hashrate(self.current_effective_hashrate)}>"


class StatChartItem:
    def __init__(self, effective: int, reported: int, valid: int, stale: int, invalid: int, timestamp: int):
        self.effective_hashrate = effective
        self.reported_hashrate = reported
        self.valid_shares = valid
        self.stale_shares = stale
        self.invalid_shares = invalid
        self.timestamp = timestamp

    def __repr__(self):
        return "<flexpoolapi.shared.StatChartItem object " \
            f"({datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y %b %d %H:%M')})>"


class Block:
    def __init__(self,
                 number: int,
                 blockhash: str,
                 block_type: str,
                 miner: str,
                 difficulty: int,
                 timestamp: int,
                 is_confirmed: bool,
                 round_time: int,
                 luck: float,
                 server_name: str,
                 block_reward: int,
                 block_fees: int,
                 uncle_inclusion_rewards: int,
                 total_rewards: int
                 ):
        self.number = number
        self.hash = blockhash
        self.type = block_type
        self.miner = miner
        self.difficulty = difficulty
        self.time = datetime.datetime.fromtimestamp(timestamp)
        self.is_confirmed = is_confirmed
        self.round_time = round_time
        self.luck = luck
        self.server_name = server_name
        self.block_reward = block_reward
        self.block_fees = block_fees
        self.uncle_inclusion_rewards = uncle_inclusion_rewards
        self.total_rewards = total_rewards

    def __repr__(self):
        return "<flexpoolapi.shared.Block object " \
            f"{self.type.capitalize()} #{self.number} ({self.hash[:5 + 2] + '…' + self.hash[-5:]})>"


class PageResponse:
    def __init__(self, contents: [], total_items: int, total_pages: int, items_per_page: int):
        self.contents = contents
        self.total_items = total_items
        self.total_pages = total_pages
        self.items_per_page = items_per_page

    def __getitem__(self, index):
        return self.contents[index]

    def __len__(self):
        return len(self.contents)

    def __repr__(self):
        return f"<flexpoolapi.shared.PageResponse object {str(self.contents)}>"

    def __str__(self):
        return str(self.contents)


def get_last_items_from_paged_response(request_url, items_count: int):
    first_page = requests.get(request_url, params=[("page", 0)])
    check_response(first_page)
    first_page = first_page.json()["result"]
    items_per_page = first_page["items_per_page"]
    total_items = first_page["total_items"]
    if items_count > total_items:
        raise(IndexError("index out of range"))

    items = first_page["data"]
    if not items_count <= items_per_page:
        total_pages_to_fetch = items_count // items_per_page
        if items_count % items_per_page:
            total_pages_to_fetch += 1
        for page_index in range(1, total_pages_to_fetch):
            fetched_page = requests.get(
                request_url, params=[("page", page_index)])
            check_response(fetched_page)
            fetched_items = fetched_page.json()["result"]["data"]
            items += fetched_items

    return items[0:items_count]


def check_response(request):
    if request.status_code not in [200, 400]:
        raise(exceptions.APIError(
            f"API Returned unexpected status code: {request.status_code} "
            f"{request.reason} (Request URL: {request.url})"))

    error = request.json()["error"]

    if error:
        raise(exceptions.APIError(
            f"API Returned error: {error} (Request URL: {request.url})"))

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

import pytest

import requests
import random
import datetime
import time
import math

import flexpoolapi.shared
import flexpoolapi.exceptions
from flexpoolapi.utils import format_hashrate

from . import utils


def test_dailyaveragestats_class_misc():
    for _ in range(0, 100):
        effective = random.randint(20000000, 5000000000)
        expected = f"<flexpoolapi.shared.DailyAverageStats object {format_hashrate(effective)}>"
        assert flexpoolapi.shared.DailyAverageStats(
            effective, 0, 0, 0, 0).__repr__() == expected


def test_stats_class_misc():
    for _ in range(0, 100):
        effective = random.randint(20000000, 5000000000)
        expected = f"<flexpoolapi.shared.Stats object {format_hashrate(effective)}>"
        assert flexpoolapi.shared.Stats(
            effective, 0, 0, 0, 0, 0, 0).__repr__() == expected


def test_startchartitem_misc():
    for _ in range(0, 100):
        timestamp = random.randint(int(time.time()) - 86400, int(time.time()))
        expected = f"<flexpoolapi.shared.StatChartItem object " \
                   f"({datetime.datetime.fromtimestamp(timestamp).strftime('%Y %b %d %H:%M')})>"
        assert flexpoolapi.shared.StatChartItem(
            0, 0, 0, 0, 0, timestamp).__repr__() == expected


def test_block_misc():
    for _ in range(0, 100):
        block_type = random.choice(["block", "uncle", "orphan"])
        block_number = random.randint(0, 10000000)
        block_hash = "0x" + utils.genrandhash()
        expected = "<flexpoolapi.shared.Block object " \
            f"{block_type.capitalize()} #{block_number} ({block_hash[:5 + 2] + '…' + block_hash[-5:]})>"
        got = flexpoolapi.shared.Block(
            block_number, block_hash, block_type, "", 0, 0, random.choice([True, False]), 0, 0, "", 0, 0, 0, 0)

        assert got.__repr__() == expected


def test_pageresponse_misc():
    for items_per_page in range(5, 20):
        data = []
        length = random.randint(0, 10)
        total_items = random.randint(length, 1000)
        for i in range(0, length):
            data.append(random.randint(0, 100))  # Just random values

        got = flexpoolapi.shared.PageResponse(
            data, length, total_pages=math.ceil(total_items / items_per_page), items_per_page=items_per_page)

        assert len(data) == len(got)
        assert str(data) == str(got)
        assert got.__repr__(
        ) == f"<flexpoolapi.shared.PageResponse object {str(data)}>"


def test_pool_wrong_miner():
    with pytest.raises(flexpoolapi.exceptions.MinerDoesNotExist):
        flexpoolapi.miner("0x0000000000000000000000000000000000000000")


def test_pool_404():
    with pytest.raises(flexpoolapi.exceptions.APIError):
        flexpoolapi.shared.check_response(
            requests.get("http://localhost:5000/404"))

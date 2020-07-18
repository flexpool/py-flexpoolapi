#
#  Software distrubuted under MIT License (MIT)
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

import math

import flexpoolapi

from . import simdata
from . import utils


class TestPoolSimulated:
    def setup_class(self):
        flexpoolapi.set_base_endpoint("http://localhost:5000/api/v1")

    def test_hashrate(self):
        got = flexpoolapi.pool.hashrate()
        assert got["EU1"] == simdata.POOL_HASHRATE_EU1
        assert got["US1"] == simdata.POOL_HASHRATE_US1
        assert got["EU1"] + got["US1"] == simdata.POOL_HASHRATE_EU1 + simdata.POOL_HASHRATE_US1

    def test_hashrate_chart(self):
        got = flexpoolapi.pool.hashrate_chart()
        assert len(got) == 144
        for i, item in enumerate(simdata.POOL_HASHRATE_CHART):
            assert item["EU1"] == got[i].servers["EU1"]
            assert item["US1"] == got[i].servers["US1"]
            assert item["total"] == got[i].total_hashrate
            assert item["timestamp"] == got[i].timestamp

    def test_miners_online(self):
        got = flexpoolapi.pool.miners_online()
        assert simdata.MINERS_ONLINE == got

    def test_workers_online(self):
        got = flexpoolapi.pool.workers_online()
        assert simdata.WORKERS_ONLINE == got

    def test_block_count(self):
        got = flexpoolapi.pool.block_count()
        assert simdata.NUM_BLOCKS == got

    def test_block_pages(self):
        page_count = math.ceil(simdata.NUM_BLOCKS / 10)
        for i in range(0, page_count):
            got = flexpoolapi.pool.blocks_paged(i)
            expected = simdata.BLOCKS[i*10:i*10+10]
            for j in range(0, len(expected)):
                utils.compare_blocks(expected[j], got[j])

    def test_latest_blocks(self):
        for n in range(1, 20):
            got = flexpoolapi.pool.last_blocks(n)
            for i in range(0, n):
                utils.compare_blocks(simdata.BLOCKS[i], got[i])

    def test_top_miners(self):
        got = flexpoolapi.pool.top_miners()
        for i, expected_miner in enumerate(simdata.TOP_MINERS):
            assert expected_miner["address"] == got[i].address
            assert expected_miner["hashrate"] == got[i].hashrate
            assert expected_miner["pool_donation"] == got[i].pool_donation
            assert expected_miner["total_workers"] == got[i].total_workers
            assert expected_miner["first_joined"] == got[i].first_joined.timestamp()

    def test_top_donators(self):
        got = flexpoolapi.pool.top_donators()
        for i, expected_miner in enumerate(simdata.TOP_DONATORS):
            assert expected_miner["address"] == got[i].address
            assert expected_miner["total_donated"] == got[i].total_donated
            assert expected_miner["pool_donation"] == got[i].pool_donation
            assert expected_miner["hashrate"] == got[i].hashrate
            assert expected_miner["first_joined"] == got[i].first_joined.timestamp()

    def test_avg_luck_roundtime(self):
        avg_luck_got, avg_roundtime_got = flexpoolapi.pool.avg_luck_roundtime()
        assert avg_luck_got == simdata.AVG_LUCK
        assert round(avg_roundtime_got, 2) == simdata.AVG_ROUNDTIME

    def test_current_luck(self):
        current_luck_got = flexpoolapi.pool.current_luck()
        assert current_luck_got == simdata.CURRENT_LUCK

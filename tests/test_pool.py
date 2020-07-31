#
#   The MIT License (MIT)
#
#   Software distrubuted under MIT License (MIT)
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
import math

import flexpoolapi

from . import utils


class TestPool:
    def setup_class(self):
        flexpoolapi.set_base_endpoint(flexpoolapi.DEFAULT_ENDPOINT)

    def test_pool_hashrate(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/hashrate").json()["result"]
        got = flexpoolapi.pool.hashrate()
        assert expected == got

    def test_pool_hashrate_chart(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/hashrateChart").json()["result"]
        got = flexpoolapi.pool.hashrate_chart()
        for i, item in enumerate(got):
            assert item.timestamp == expected[i]["timestamp"]
            assert item.total_hashrate == expected[i]["total"]
            for server_name, hashrate in item.servers.items():
                assert expected[i][server_name] == hashrate

    def test_online_miners(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/minersOnline").json()["result"]
        got = flexpoolapi.pool.miners_online()
        assert expected == got

    def test_online_workers(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/workersOnline").json()["result"]
        got = flexpoolapi.pool.workers_online()
        assert expected == got

    def test_block_pages(self):
        meta = requests.get("https://flexpool.io/api/v1/pool/blocks",
                            params=[("page", 0)]).json()["result"]
        total_items = meta["total_items"]
        items_per_page = meta["items_per_page"]

        pages_to_fetch = math.ceil(total_items / items_per_page)

        for page in range(0, pages_to_fetch):
            expected = requests.get(
                "https://flexpool.io/api/v1/pool/blocks", params=[("page", page)]
            ).json()["result"]["data"]
            got = flexpoolapi.pool.blocks_paged(page=page)
            for i in range(0, len(expected)):
                utils.compare_blocks(expected[i], got[i])

    def test_last_blocks(self):
        # TESTING_AMOUNTS = [3, 1, 6, 8, 0, 5, 10, 2, 9, 4]
        TESTING_AMOUNTS = [2, 3, 1]
        expected = requests.get("https://flexpool.io/api/v1/pool/blocks",
                                params=[("page", 0)]).json()["result"]["data"]
        for testing_amount in TESTING_AMOUNTS:
            got = flexpoolapi.pool.last_blocks(count=testing_amount)
            for i, block_expected in enumerate(expected[0:testing_amount]):
                utils.compare_blocks(block_expected, got[i])

    def test_block_count(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/blockCount").json()["result"]
        got = flexpoolapi.pool.block_count()
        assert expected["confirmed"] == got["confirmed"]
        assert expected["unconfirmed"] == got["unconfirmed"]

    def test_top_miners(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/topMiners").json()["result"]
        got = flexpoolapi.pool.top_miners()
        for i, top_miner in enumerate(expected):
            assert top_miner["address"] == got[i].address
            assert top_miner["hashrate"] == got[i].hashrate
            assert top_miner["pool_donation"] == got[i].pool_donation
            assert top_miner["total_workers"] == got[i].total_workers
            assert top_miner["first_joined"] == got[i].first_joined.timestamp()

    def test_top_donators(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/topDonators").json()["result"]
        got = flexpoolapi.pool.top_donators()
        for i, top_miner in enumerate(expected):
            assert top_miner["address"] == got[i].address
            assert top_miner["total_donated"] == got[i].total_donated
            assert top_miner["pool_donation"] == got[i].pool_donation
            assert top_miner["balance"] == got[i].balance
            assert top_miner["hashrate"] == got[i].hashrate
            assert top_miner["first_joined"] == got[i].first_joined.timestamp()

    def test_avg_luck_roundtime(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/avgLuckRoundtime").json()["result"]
        avg_luck_got, avg_roundtime_got = flexpoolapi.pool.avg_luck_roundtime()
        assert expected["luck"] == avg_luck_got
        assert round(expected["round_time"], 2) == avg_roundtime_got

    def test_current_luck(self):
        expected = requests.get(
            "https://flexpool.io/api/v1/pool/currentLuck").json()["result"]
        got = flexpoolapi.pool.current_luck()
        assert expected == got

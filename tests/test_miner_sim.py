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
import flexpoolapi
import math

from . import simdata
from . import utils


class TestMinerSimulated:
    def setup_class(self):
        flexpoolapi.set_base_endpoint("http://localhost:5000/api/v1")
        self.miner_api = flexpoolapi.miner(simdata.MINER_ADDRESS)

    def test_balance(self):
        assert self.miner_api.balance() == simdata.MINER_BALANCE

    def test_current_hashrate(self):
        effective, reported = self.miner_api.current_hashrate()
        assert effective == simdata.CURRENT_EFFECTIVE_HASHRATE
        assert reported == simdata.CURRENT_REPORTED_HASHRATE

    def test_daily_hashrate(self):
        got = self.miner_api.daily_average_stats()
        assert got.effective_hashrate == simdata.DAILY_EFFECTIVE_HASHRATE
        assert got.reported_hashrate == simdata.DAILY_REPORTED_HASHRATE
        assert got.valid_shares == simdata.DAILY_VALID_SHARES
        assert got.stale_shares == simdata.DAILY_STALE_SHARES
        assert got.invalid_shares == simdata.DAILY_INVALID_SHARES

    def test_stats(self):
        got = self.miner_api.stats()
        assert got.current_effective_hashrate == simdata.CURRENT_EFFECTIVE_HASHRATE
        assert got.current_reported_hashrate == simdata.CURRENT_REPORTED_HASHRATE
        assert got.average_effective_hashrate == simdata.DAILY_EFFECTIVE_HASHRATE
        assert got.average_reported_hashrate == simdata.DAILY_REPORTED_HASHRATE
        assert got.valid_shares == simdata.DAILY_VALID_SHARES
        assert got.stale_shares == simdata.DAILY_STALE_SHARES
        assert got.invalid_shares == simdata.DAILY_INVALID_SHARES

    def test_worker_count(self):
        assert self.miner_api.worker_count() == simdata.WORKER_COUNT

    def test_workers(self):
        got = self.miner_api.workers()
        for i, expected_worker in enumerate(simdata.WORKERS):
            assert got[i].worker_name == expected_worker["name"]
            assert got[i].is_online == expected_worker["online"]

    def test_chart(self):
        got = self.miner_api.chart()
        for i in range(0, 144):
            assert got[i].reported_hashrate == simdata.MINER_CHART[i]["reported_hashrate"]
            assert got[i].effective_hashrate == simdata.MINER_CHART[i]["effective_hashrate"]
            assert got[i].valid_shares == simdata.MINER_CHART[i]["valid_shares"]
            assert got[i].stale_shares == simdata.MINER_CHART[i]["stale_shares"]
            assert got[i].invalid_shares == simdata.MINER_CHART[i]["invalid_shares"]

    def test_payment_count(self):
        assert self.miner_api.payment_count() == simdata.PAYMENT_COUNT

    def test_payments_pages(self):
        page_count = math.ceil(simdata.PAYMENT_COUNT / 10)
        for i in range(0, page_count):
            got = self.miner_api.payments_paged(i)
            expected = simdata.PAYMENTS[i * 10:i * 10 + 10]
            for j in range(0, len(expected)):
                assert expected[j]["amount"] == got[j].amount
                assert expected[j]["timestamp"] == got[j].time.timestamp()
                assert expected[j]["duration"] == got[j].duration
                assert expected[j]["txid"] == got[j].txid

    def test_block_count(self):
        assert self.miner_api.block_count() == simdata.MINER_BLOCK_COUNT

    def test_blocks_pages(self):
        page_count = math.ceil(simdata.MINER_BLOCK_COUNT / 10)
        for i in range(0, page_count):
            got = self.miner_api.blocks_paged(i)
            expected = simdata.MINER_BLOCKS[i * 10:i * 10 + 10]
            for j in range(0, len(expected)):
                utils.compare_blocks(expected[j], got[j])

    def test_details(self):
        got = self.miner_api.details()
        assert got.censored_email == simdata.MINER_CENSORED_EMAIL
        assert got.censored_ip == simdata.MINER_CENSORED_IP
        assert got.pool_donation == simdata.MINER_POOL_DONATION
        assert got.min_payout_threshold == simdata.MINER_MIN_PAYOUT_THRESHOLD
        assert got.first_joined_date.timestamp() == simdata.MINER_FIRST_JOINED

    def test_estimated_daily_profits(self):
        got = self.miner_api.estimated_daily_profit()
        assert got == simdata.MINER_ESTIMATED_DAILY_PROFIT

    def test_total_paid(self):
        got = self.miner_api.total_paid()
        assert got == simdata.MINER_TOTAL_PAID

    def test_total_donated(self):
        got = self.miner_api.total_donated()
        assert got == simdata.MINER_TOTAL_DONATED

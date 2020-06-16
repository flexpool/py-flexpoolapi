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

from . import simdata
from . import utils


class TestWorkerSimulated:
    def setup_class(self):
        flexpoolapi.set_base_endpoint("http://localhost:5000/api/v1")
        self.workers = flexpoolapi.miner(simdata.MINER_ADDRESS).workers()

    def test_current_hashrate(self):
        for i in range(0, len(self.workers)):
            effective, reported = self.workers[i].current_hashrate()

            assert simdata.WORKERS[i]["effective_hashrate"] == effective
            assert simdata.WORKERS[i]["reported_hashrate"] == reported

    def test_daily_stats(self):
        for i in range(0, len(self.workers)):
            got = self.workers[i].daily_average_stats()

            assert simdata.WORKERS[i]["daily_effective_hashrate"] == got.effective_hashrate
            assert simdata.WORKERS[i]["daily_reported_hashrate"] == got.reported_hashrate
            assert simdata.WORKERS[i]["valid_shares"] == got.valid_shares
            assert simdata.WORKERS[i]["stale_shares"] == got.stale_shares
            assert simdata.WORKERS[i]["invalid_shares"] == got.invalid_shares

    def test_stats(self):
        for i in range(0, len(self.workers)):
            got = self.workers[i].stats()

            assert simdata.WORKERS[i]["effective_hashrate"] == got.current_effective_hashrate
            assert simdata.WORKERS[i]["reported_hashrate"] == got.current_reported_hashrate
            assert simdata.WORKERS[i]["daily_effective_hashrate"] == got.average_effective_hashrate
            assert simdata.WORKERS[i]["daily_reported_hashrate"] == got.average_reported_hashrate
            assert simdata.WORKERS[i]["valid_shares"] == got.valid_shares
            assert simdata.WORKERS[i]["stale_shares"] == got.stale_shares
            assert simdata.WORKERS[i]["invalid_shares"] == got.invalid_shares

    def test_chart(self):
        for i in range(0, len(self.workers)):
            got = self.workers[i].chart()
            for j in range(0, 144):
                expected = simdata.WORKERS_CHART_MAP[self.workers[i].worker_name][j]
                assert got[j].reported_hashrate == expected["reported_hashrate"]
                assert got[j].effective_hashrate == expected["effective_hashrate"]
                assert got[j].valid_shares == expected["valid_shares"]
                assert got[j].stale_shares == expected["stale_shares"]
                assert got[j].invalid_shares == expected["invalid_shares"]
                assert got[j].timestamp == expected["timestamp"]


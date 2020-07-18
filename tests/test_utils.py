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

import flexpoolapi.utils


@pytest.mark.parametrize(
    "value, expected",
    (
        (554567074381, "554.6 GH/s"),
        (736874205710, "736.9 GH/s"),
        (947896881215, "947.9 GH/s"),
        (48593396, "48.6 MH/s"),
        (61210, "61.2 kH/s")
    )
)
def test_format_hashrate(value, expected):
    assert flexpoolapi.utils.format_hashrate(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    (
        (3242668809488253150, "3.24267 ETH"),
        (9477325763736408077, "9.47733 ETH"),
        (3734333446367471820, "3.73433 ETH"),
        (2298779027626753117, "2.29878 ETH"),
        (521126336805019143,  "0.52113 ETH")
    )
)
def test_format_hashrate(value, expected):
    assert flexpoolapi.utils.format_weis(value, prec=5) == expected

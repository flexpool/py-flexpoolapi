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

import pytest

from . import utils


@pytest.mark.parametrize(
    "addr, expected",
    (
        ("0xfd7af55540c2383adb69b5de147886d40b259528",
         "0xfd7AF55540C2383adB69b5De147886D40b259528"),
        ("0x2be3dd6c2a720c038b598b9951d300286b9ebb7a",
         "0x2BE3DD6c2a720c038B598B9951D300286B9EbB7A"),
        ("0x254471ce054b4e3b2f24c34d0b95defca218dfc1",
         "0x254471cE054B4e3B2F24c34d0B95defcA218DFC1"),
        ("0xba553e99a6e6ebbd228b2ae9cd317e62bdfb1175",
         "0xba553E99A6E6EbBd228b2aE9Cd317E62BDFB1175"),
        ("0x69cb74e05bd8d769f17582ec4d26ec3b65dd0f03",
         "0x69Cb74e05BD8d769f17582EC4D26eC3B65Dd0f03")
    )
)
def test_utils_to_checksum_address(addr, expected):
    assert utils.to_checksum_address(addr) == expected

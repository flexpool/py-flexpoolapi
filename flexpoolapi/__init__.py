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

from . import poolapi as _pool_module
from . import minerapi as _miner_module
from . import workerapi as _worker_module

pool = _pool_module.PoolAPI()
miner = _miner_module.MinerAPI


def set_base_endpoint(endpoint):
    global pool, miner
    _pool_module.update_endpoint(endpoint)
    _miner_module.update_endpoint(endpoint)
    _worker_module.update_endpoint(endpoint)
    pool = _pool_module.PoolAPI()


DEFAULT_ENDPOINT = "https://flexpool.io/api/v1"

set_base_endpoint(DEFAULT_ENDPOINT)

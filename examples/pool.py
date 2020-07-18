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

import flexpoolapi

print("Pool hashrate:", flexpoolapi.pool.hashrate())
print("Pool hashrate chart:", flexpoolapi.pool.hashrate_chart())

print("Pool online miners:", flexpoolapi.pool.miners_online())
print("Pool workers:", flexpoolapi.pool.workers_online())

print("Total blocks:", flexpoolapi.pool.block_count())

last_blocks_page = flexpoolapi.pool.blocks_paged(page=0)
print("Last block page:", last_blocks_page)

last_2_blocks = flexpoolapi.pool.last_blocks(count=2)
print("Last 2 blocks", last_2_blocks)

top_miners = flexpoolapi.pool.top_miners()
print("Top miners:", top_miners)
top_donators = flexpoolapi.pool.top_donators()
print("Top donators:", top_donators)

avg_luck, avg_roundtime = flexpoolapi.pool.avg_luck_roundtime()
print("AVG Luck:", avg_luck)
print("AVF Round Time:", avg_roundtime)

current_luck = flexpoolapi.pool.current_luck()
print("Current Luck:", current_luck)

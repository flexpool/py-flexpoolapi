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
from flexpoolapi import utils

miner = flexpoolapi.miner(flexpoolapi.pool.top_miners()[0].address)

print("Using address", miner.address, "(Top miner)")

print("\n--DETAILS--\n")

details = miner.details()
print("Min Payout Threshold:", details.min_payout_threshold)
print("Pool Donation:", str(details.pool_donation * 100) + "%")
print("Censored Email:", details.censored_email)
print("Censored IP:", details.censored_ip)
print("First joined:", details.first_joined_date)

print("\n--HEADER--\n")

print("Unpaid balance:", utils.format_weis(miner.balance()))

print("\n--CURRENT HASHRATE--\n")

effective_hashrate, reported_hashrate = miner.current_hashrate()
print("Effective hashrate", effective_hashrate)
print("Reported hashrate", reported_hashrate)

print("\n--DAILY STATS--\n")

daily_average_stats = miner.daily_average_stats()
print("Daily Avg Effective hashrate", daily_average_stats.effective_hashrate)
print("Daily Avg Reported hashrate", daily_average_stats.reported_hashrate)
print("Daily Valid shares", daily_average_stats.valid_shares)
print("Daily Stale shares", daily_average_stats.stale_shares)
print("Daily Invalid shares", daily_average_stats.invalid_shares)

print("\n--STATS--\n")

stats = miner.stats()
print("Current Effective hashrate", stats.current_effective_hashrate)
print("Current Reportted hashrate", stats.current_reported_hashrate)
print("Daily Avg Effective hashrate", stats.average_effective_hashrate)
print("Daily Avg Reported hashrate", stats.average_reported_hashrate)
print("Daily Valid shares", stats.valid_shares)
print("Daily Stale shares", stats.stale_shares)
print("Daily Invalid shares", stats.invalid_shares)

print("\n---BLOCKS--\n")

print("Blocks Count", miner.block_count())
print("Blocks (page 0)", miner.blocks_paged(0))
print("Last 1 block", miner.last_blocks(count=1))

print("\n--OTHER--\n")

print("Workers count", miner.worker_count())
print("Chart:", miner.chart())

print("Total payments:", miner.payment_count())
print("Payments page 0:", miner.payments_paged(0))
print("Last 2 payments:", miner.last_payments(2))

print("Estimated daily profit:", miner.estimated_daily_profit())
print("Round share:", miner.round_share())

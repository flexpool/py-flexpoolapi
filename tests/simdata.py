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

import random
import time

from . import utils

POOL_HASHRATE_EU1 = random.randint(0, 50000000000000)  # 0 H/s to 50 TH/s
POOL_HASHRATE_US1 = random.randint(0, 50000000000000)  # 0 H/s to 50 TH/s

MINERS_ONLINE = random.randint(0, 50000)
while True:
    # WORKERS_ONLINE should be >= MINERS_ONLINE
    WORKERS_ONLINE = random.randint(0, 100000)
    if WORKERS_ONLINE >= MINERS_ONLINE:
        break

POOL_HASHRATE_CHART = []

start_ts = int(time.time())
start_ts -= start_ts % 600  # Make it latest 10 min timestamp

for i in range(0, 144):
    eu1 = random.randint(0, POOL_HASHRATE_EU1 * 2)
    us1 = random.randint(0, POOL_HASHRATE_US1 * 2)
    POOL_HASHRATE_CHART.append({
        "timestamp": start_ts - 600 * i,
        "EU1": eu1,
        "US1": us1,
        "total": eu1 + us1
    })


NUM_BLOCKS = random.randint(100, 200)  # Using not big values for tests

BLOCKS_STARTFROM = random.randint(10000000, 10200000)  # 10M to 10.2M

ETHEREUM_10000000_BLOCK_TIMESTAMP = 1588598533  # 2020 May 04 16:05:13

BLOCKS = []

UNCONFIRMED_COUNT = random.randint(1, 5)

for i in range(0, NUM_BLOCKS):
    block_num = BLOCKS_STARTFROM + i
    block_type = random.choice(["block", "block", "block", "block", "block", "block", "block", "block", "block",
                                "block", "block", "block", "block", "uncle", "uncle", "uncle", "uncle", "orphan"])
    if block_type == "uncle":
        block_reward = random.choice([1.75, 1.5]) * 10**18
    else:
        block_reward = 2 * 10**18

    if block_type != "uncle":
        uncle_inclusion_rewards = random.choice(
            [0, 0, 0, 0, 0, 0, 0.625, 0.625, 0.125])
    else:
        uncle_inclusion_rewards = 0

    if block_type != "uncle":
        block_fees = random.randint(0, 0.5 * 10**18)
    else:
        block_fees = 0

    block = {
        "number": block_num,
        "type": block_type,
        "miner": utils.genrandaddr(),
        "difficulty": random.randint(2000000000000000, 2500000000000000),
        "timestamp": (block_num - 10000000) * 12 + ETHEREUM_10000000_BLOCK_TIMESTAMP,
        "confirmed": True,
        "round_time": random.randint(5, 120),
        "luck": random.randint(500000000000000, 10000000000000000) / 1000000000000000,
        "server_name": random.choice(["EU1", "US1"]),
        "block_reward": block_reward,
        "block_fees": block_fees,
        "uncle_inclusion_rewards": uncle_inclusion_rewards,
        "total_rewards": block_reward + uncle_inclusion_rewards + block_fees,
        "hash": utils.genrandhash()
    }

    if i >= NUM_BLOCKS - 1 - UNCONFIRMED_COUNT:
        block["confirmed"] = False

    BLOCKS.append(block)

TOP_MINERS = []

hashrates = []
for i in range(0, 10):
    hashrates.append(random.randint(15000000000, 50000000000)
                     )  # 15 GH/s to 50 GH/s

hashrates = sorted(hashrates)
hashrates.reverse()

for i in range(0, 10):
    hashrate = hashrates[i]
    TOP_MINERS.append({
        "address": utils.genrandaddr(),
        "hashrate": hashrate,
        "pool_donation": random.choice([0.01, 0.02, 0.03, 0.04, 0.05]),
        # 20 MH/s to 90 MH/s
        "total_workers": hashrate / random.randint(20000000, 90000000),
        "first_joined": random.randint(int(time.time()) - 86400 * 365, int(time.time()))
    })


TOP_DONATORS = []

total_donated_top = []
for i in range(0, 10):
    total_donated_top.append(random.randint(
        50 * 10**18, 100 * 10**18))  # 50 ETH to 100 ETH

total_donated_top = sorted(total_donated_top)
total_donated_top.reverse()

for i in range(0, 10):
    TOP_DONATORS.append({
        "address": utils.genrandaddr(),
        "total_donated": total_donated_top[i],
        "pool_donation": random.choice([0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]),
        "hashrate": random.randint(1000000000, 15000000000),
        "first_joined": random.randint(int(time.time()) - 86400 * 365, int(time.time()))
    })


AVG_LUCK = random.randint(
    500000000000000, 10000000000000000) / 1000000000000000
AVG_ROUNDTIME = random.randint(50, 1200) / 10


MINER_ADDRESS = utils.genrandaddr()
MINER_BALANCE = random.randint(0, 10**18)  # 0 ETH to 1 ETH

CURRENT_REPORTED_HASHRATE = random.randint(
    50000000, 5000000000)  # 50 MH/s to 5 GH/s
if random.choice([True, False]):
    # Effective is higher than reported (True was selected)
    print(int(CURRENT_REPORTED_HASHRATE * 0.1))
    CURRENT_EFFECTIVE_HASHRATE = CURRENT_REPORTED_HASHRATE + \
        random.randint(0, int(CURRENT_REPORTED_HASHRATE * 0.1))
else:
    CURRENT_EFFECTIVE_HASHRATE = CURRENT_REPORTED_HASHRATE + \
        random.randint(0, int(CURRENT_REPORTED_HASHRATE * 0.1))


DAILY_REPORTED_HASHRATE = random.randint(
    CURRENT_REPORTED_HASHRATE - int(CURRENT_REPORTED_HASHRATE * 0.1),
    CURRENT_REPORTED_HASHRATE + int(CURRENT_REPORTED_HASHRATE * 0.1))

DAILY_EFFECTIVE_HASHRATE = random.randint(
    CURRENT_EFFECTIVE_HASHRATE - int(CURRENT_EFFECTIVE_HASHRATE * 0.1),
    CURRENT_EFFECTIVE_HASHRATE + int(CURRENT_EFFECTIVE_HASHRATE * 0.1))

DAILY_VALID_SHARES = int(DAILY_EFFECTIVE_HASHRATE * 86400 / 4000000000)
DAILY_STALE_SHARES = int(DAILY_VALID_SHARES * (random.randint(1, 5) / 1000))
DAILY_INVALID_SHARES = int(DAILY_VALID_SHARES * (random.randint(0, 1) / 1000))

MINER_CHART = []

for i in range(0, 144):
    MINER_CHART.append({
        "reported_hashrate": DAILY_REPORTED_HASHRATE * (random.randint(90, 110) / 100),
        "effective_hashrate": DAILY_EFFECTIVE_HASHRATE * (random.randint(90, 110) / 100),
        "valid_shares": DAILY_VALID_SHARES / 144,
        "stale_shares": DAILY_STALE_SHARES / 144,
        "invalid_shares": DAILY_INVALID_SHARES / 144,
        "timestamp": start_ts - 600 * i
    })


PAYMENT_COUNT = random.randint(15, 100)
PAYMENTS = []

last_timestamp = int(time.time())

for i in range(0, PAYMENT_COUNT):
    timestamp = random.randint(last_timestamp - 86400 * 7, last_timestamp)
    PAYMENTS.append({
        "amount": random.randint(10**18, 10 * 10**18),
        "timestamp": timestamp,
        "duration": last_timestamp - timestamp,  # durations are one index down
        "txid": utils.genrandhash()
    })

    last_timestamp = timestamp


MINER_BLOCKS = []

for pool_block in BLOCKS:
    if random.choice([True, False]):
        pool_block["address"] = MINER_ADDRESS
        MINER_BLOCKS.append(pool_block)


MINER_BLOCK_COUNT = len(MINER_BLOCKS)

MINER_CENSORED_EMAIL = "mai*@exa****.com"  # mail@example.com
MINER_CENSORED_IP = "*.*.*.1"  # 1.1.1.1
MINER_POOL_DONATION = 0.05  # MVP
MINER_MIN_PAYOUT_THRESHOLD = 0.05  # Minimal one
MINER_FIRST_JOINED = random.randint(
    last_timestamp - 86400 * 365, last_timestamp)

WORKER_COUNT = random.randint(1, 10)
WORKERS = []

WORKER_NAME_STYLES = [
    "rig%",
    "rig-%",
    "worker%",
    "worker-%"
]

SELECTED_WORKER_NAME_STYLE = random.choice(WORKER_NAME_STYLES)

for worker_i in range(0, WORKER_COUNT):
    WORKERS.append({
        "name": SELECTED_WORKER_NAME_STYLE.replace("%", str(worker_i)),
        "online": True,
        "effective_hashrate": CURRENT_EFFECTIVE_HASHRATE / WORKER_COUNT,
        "reported_hashrate": CURRENT_REPORTED_HASHRATE / WORKER_COUNT,
        "daily_effective_hashrate": CURRENT_EFFECTIVE_HASHRATE / WORKER_COUNT * random.randint(90, 110) / 100,
        "daily_reported_hashrate": CURRENT_REPORTED_HASHRATE / WORKER_COUNT * random.randint(90, 110) / 100,
        "valid_shares": DAILY_VALID_SHARES // WORKER_COUNT,
        "stale_shares":  DAILY_STALE_SHARES // WORKER_COUNT,
        "invalid_shares": DAILY_INVALID_SHARES // WORKER_COUNT,
        "last_seen": random.randint(int(time.time()) - 600, int(time.time()))
    })

WORKERS_MAP = {v["name"]: v for v in WORKERS}

WORKERS_CHART_MAP = {}

for worker_name, worker_data in WORKERS_MAP.items():
    tmp = []
    for i in range(0, 144):
        tmp.append({
            "reported_hashrate": worker_data["reported_hashrate"] * random.randint(90, 110) / 100,
            "effective_hashrate": worker_data["effective_hashrate"] * random.randint(90, 110) / 100,
            "valid_shares": int(worker_data["valid_shares"] * random.randint(90, 110) / 100),
            "stale_shares": int(worker_data["stale_shares"] * random.randint(90, 110) / 100),
            "invalid_shares": int(worker_data["invalid_shares"] * random.randint(90, 110) / 100),
            "timestamp": start_ts - i * 600
        })
    WORKERS_CHART_MAP[worker_name] = tmp


CURRENT_LUCK = random.randint(1, 100000000) / 10000000

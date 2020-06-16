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

import random
from sha3 import keccak_256

import flexpoolapi


def compare_blocks(raw_block, block: flexpoolapi.shared.Block):
    assert raw_block["number"] == block.number
    assert raw_block["hash"] == block.hash
    assert raw_block["miner"] == block.miner
    assert raw_block["type"] == block.type
    assert raw_block["difficulty"] == block.difficulty
    assert int(raw_block["timestamp"]) == int(block.time.timestamp())
    assert raw_block["confirmed"] == block.is_confirmed
    assert raw_block["round_time"] == block.round_time
    assert raw_block["luck"] == block.luck
    assert raw_block["server_name"] == block.server_name
    assert raw_block["block_reward"] == block.block_reward
    assert raw_block["block_fees"] == block.block_fees
    assert raw_block["uncle_inclusion_rewards"] == block.uncle_inclusion_rewards
    assert raw_block["total_rewards"] == block.total_rewards


def clear_0x(val):
    if val[:2] == "0x":
        return val[2:]

    return val


def to_checksum_address(addr):
    addr = clear_0x(addr)
    addrhash = keccak_256(bytes(addr, "utf-8")).hexdigest()
    out = ""
    for i in range(0, 40):
        if int(addrhash[i], 16) > 7:
            out += addr[i].upper()
        else:
            out += addr[i].lower()

    return "0x" + out


def genrandaddr():
    n = random.getrandbits(160)
    hexaddr = hex(n)[2:]
    hexaddr = "0" * (40 - len(hexaddr)) + hexaddr

    return to_checksum_address(hexaddr)


def genrandhash():
    n = random.getrandbits(256)
    hexhash = hex(n)[2:]
    hexhash = "0" * (64 - len(hexhash)) + hexhash

    return hexhash

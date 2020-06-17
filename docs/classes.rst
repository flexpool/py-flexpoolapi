..  The MIT License (MIT)

..  Copyright (c) 2020 Flexpool

.. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
   documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
   and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

.. The above copyright notice and this permission notice shall be included in all copies or substantial portions of
   the Software.

.. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
   THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.


Classes
==========================================


For easy interfacing, all structured responses are wrapped into classes.

**Shared**
------------------------------------------

These classes are used all around the **py-flexpoolapi**

.. _block:

shared.Block
------------------------------------------

.. py:class:: flexpoolapi.shared.Block

**Properties**

- **number:** *int*

   Block number (aka block height).

- **hash:** *str*

   Block hash.

- **type:** *str*

   Block type. One of ``['block', 'uncle', 'orphan']``

- **miner:** *str*

   Block miner's checksummed Ethereum address.

   (e.g ``0x3f7d727B73A30E8BF801760F59962C15a56DbA74``)

- **difficulty:** *int*

   Block difficulty.

   (e.g. ``2312863022593449``)

- **time:** datetime.datetime

   Date when block was mined.

- **is_confirmed:** *bool*

   Block confirmation.

- **round_time:** *int*

   Round time in seconds (e.g ``153``)

- **luck:** *float*

   Block luck.

   (e.g. ``1.743672971``, which is 174%)

- **server_name**: *str*

   Name of server that mined this block.

   (e.g. ``EU1``, ``US1``)

- **block_reward:** *int*

   Block reward in wei.

   (e.g. ``2000000000000000000``)

- **block_fees:** *int*

   Block fees in wei.

- **uncle_inclusion_rewards:** *int*

   Uncle inclusion rewards (e.g ``62500000000000000``, which is 0.0625 ETH)

- **total_rewards:** *int*

   Sum of all rewards.

.. _stats:

shared.Stats
------------------------------------------

.. py:class:: flexpoolapi.shared.Stats

**Properties**

- **current_effective_hashrate:** *int*

   Current effective hashrate

- **current_reported_hashrate:** *int*

   Current reported hashrate

- **average_effective_hashrate:** *int*

   24h average effective hashrate

- **average_reported_hashrate:** *int*

   24h average reported hashrate

- **valid_shares:** *int*

   Total amount of valid shares

- **stale_shares:** *int*

   Total amount of stale shares

- **invalid_shares:** *int*

   Total amount of invalid shares


.. _daily_average_stats:

shared.DailyAverageStats
------------------------------------------

.. py:class:: flexpoolapi.shared.DailyAverageStats

- **effective_hashrate:** *int*

   24h average effective hashrate

- **reported_hashrate:** *int*

   24h average reported hashrate

- **valid_shares:** *int*

   Amount of valid shares submitted during the day.

- **stale_shares:** *int*

   Amount of stale shares submitted during the day.

- **invalid_shares:** *int*

   Amount of invalid shares submitted during the day.

.. _stat_chart_item:

shared.StatChartItem
------------------------------------------


.. py:class:: flexpoolapi.shared.StatChartItem

- **effective_hashrate:** *int*

   Effective hashrate

- **reported_hashrate:** *int*

   Reported hashrate

- **valid_shares:** *int*

   Amount of valid shares submitted during the item time (10min).

- **stale_shares:** *int*

   Amount of stale shares submitted during the item time (10min).

- **invalid_shares:** *int*

   Amount of invalid shares submitted during the item time (10min).


.. _page_response:

shared.PageResponse
------------------------------------------

.. py:class:: flexpoolapi.shared.PageResponse

.. note::
   This class can be used as a regular list.

   .. code-block:: python

      >>> len(page_response)
      '<amount of items>'
      >>> page_response[0]
      '<item with index 0>'
      >>> page_response[1]
      '<item with index 1>'

**Properties**

- **contents:** *[<any>]*

   Stores the ``PageResponse`` items.

- **total_items:** *int*

   The amount of items in ``contents``. Cannot be bigger than ``items_per_page``.


- **total_pages:** *int*

   The total amount of pages.

- **items_per_page:** *int*

   Amount of items per page. Normally equals to **10**.


**Pool**
------------------------------------------

Classes used by ``flexpoolapi.pool`` namespace.

.. _top_miner:

pool.TopMiner
------------------------------------------

.. py:class:: flexpoolapi.pool.TopMiner

**Properties**

- **address:** *str*

   Checksummed Miner's Ethereum address.

- **hashrate:** *int*

   Miner's current effective hashrate.

- **pool_donation:** *int*

   Miner's Pool Donation.

   (e.g. 0.05, which is 5%)

- **total_workers:** *int*

   The amount of workers.

- **first_joined:** *datetime.datetime*

   Date when the miner firstly mined on pool.


.. _top_donator:

pool.TopDonator
------------------------------------------

.. py:class:: flexpoolapi.pool.TopDonator

**Properties**

- **address:** *str*

   Checksummed Miner's Ethereum address.

- **total_donated:** *int*

   Total donated amount (weis).

   (e.g ``528498812374981273489``, which is 528.5 ETH)

- **pool_donation:** *int*

   Miner's Pool Donation.

   (e.g. 0.05, which is 5%)

- **hashrate:** *int*

   Miner's current effective hashrate.

- **first_joined:** *datetime.datetime*

   Date when the miner firstly mined on pool.

.. _hashrate_chart_item:

pool.HashrateChartItem
------------------------------------------

.. py:class:: flexpoolapi.pool.HashrateChartItem

**Properties**

- **servers:** *{str: int}*

   Pool hashrate splitted by servers. A dictionary with ``{"server": <hashrate>}`` scheme.

- **total_hashrate:** *int*

   Total pool's hashrate.


- **timestamp:** *int*

   Unix timestamp of item.


**Miner**
------------------------------------------

Classes used by ``flexpoolapi.miner`` class.

.. _miner_details:

miner.MinerDetails
------------------------------------------

.. py:class:: flexpoolapi.miner.MinerDetails

**Properties**

- **addresss:** *str*

   The Miner's Ethereum address.

- **min_payout_threshold**: *int*

   Miner's minimal payout threshold (represented in wei).

   (e.g. ``200000000000000000``, which is 0.2 ETH)

- **pool_donation**: *int*

   Miner's pool donation.

   (e.g. ``0.05``, which is 5%)

- **censored_email:** *int*

   Miner's censored email.

   (e.g. ``mai*@exa****.com``)

- **censored_ip:** *int*

   Miner's censored IP address.

   (e.g. ``*.*.*.1``)


- **first_joined_date:** *datetime.datetime*

   Date when miner's firstly mined on the pool.


.. _transaction:

miner.Transaction
------------------------------------------

.. py:class:: flexpoolapi.miner.Transaction

**Properties**

- **amount:** *int*

   Transaction value (represented in wei).

   (e.g. ``912347012097312304``, which is 0.91 ETH)

- **time:** *datetime.datetime*

   Time when the transaction was sent.

- **duration:** *int*

   The duration between current and previous payout (secs). Equals to 0 if it is the first payout.

- **txid**: *str*

   Transaction hash.

   (e.g. ``3d02b5f888169e8ab55ae39a8f93eeab1f24703081798c61ac1a390d1b2e909b``)
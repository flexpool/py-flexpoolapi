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


Pool Module
==========================================

.. py:class:: flexpoolapi.pool

    The API's ``Pool Module`` bindings.

General statistics
------------------------------------------

.. py:method:: pool.hashrate()

      - Delegates to ``/pool/hashrate`` API Method

    Returns pool's current effective hashrate in H/s (hashes per second).
    All data is splitted into servers (e.g. EU1, US2)

    .. code-block:: python

        >>> flexpoolapi.pool.hashrate()
        {'EU1': 21818049812367, 'US1': 19274829582345, 'total': 41092879394712}


.. py:method:: pool.miners_online()

      - Delegates to ``/pool/minersOnline`` API Method

      Returns the amount of miners currently mining on our pool.

      .. code-block:: python

         >>> flexpoolapi.pool.miners_online()
         47192


.. py:method:: pool.workers_online()

      - Delegates to ``/pool/workersOnline`` API Method

      Returns the amount of workers currently mining on our pool.

      .. code-block:: python

         >>> flexpoolapi.pool.workers_online()
         253194

.. py:method:: pool.block_count()

      - Delegates to ``/pool/blockCount`` API Method

      Returns the amount of blocks that were mined by pool.

      .. code-block:: python

         >>> flexpoolapi.pool.block_count()
         528191


.. py:method:: pool.current_luck()

      - Delegates to ``/pool/currentLuck`` API Method

      Returns current luck.

      .. code-block:: python

         >>> flexpoolapi.pool.current_luck()
         2.911822938883974 # 291%


.. py:method:: pool.avg_luck_roundtime()

      - Delegates to ``/pool/avgLuckRoundtime`` API Method

      Returns average luck and round time.

      .. hint::

            Round time is the time between pool's blocks

      .. code-block:: python

         >>> luck, round_time = flexpoolapi.pool.avg_luck_roundtime()
         >>> luck
         1.297540974974846  # 129%
         >>> round_time
         55.4  # 55.4 secs


Top Statistics
------------------------------------------

.. py:method:: pool.top_miners()

      - Delegates to ``/pool/topMiners`` API method

      Returns top miners by hashrate (descending order).

      .. code-block:: python

         >>> top_miners = flexpoolapi.pool.top_miners()
         [<flexpoolapi.pool.TopMiner object 0xD7557BcC922E16D5248231Ee85919F5b01c97d12: 4.8 TH/s>, <flexpoolapi.pool.TopMiner object 0x31bfB275184Ce145B689ea79963c7b8ba5Fc5C99: 983.2 GH/s>, ...]

         >>> top_miners[0]
         <flexpoolapi.pool.TopMiner object 0xD7557BcC922E16D5248231Ee85919F5b01c97d12: 4.8 TH/s>

         >>> top_miners[0].address
         0xD7557BcC922E16D5248231Ee85919F5b01c97d12
         >>> top_miners[0].hashrate
         4832143791236
         >>> top_miners[0].pool_donation
         0.05
         >>> top_miners[0].total_workers
         24821
         >>> top_miners[0].first_joined
         datetime.datetime(2020, 5, 13, 20, 8, 7)

      **References:**

         :ref:`top_miner`


.. py:method:: pool.top_donators()

      - Delegates to ``/pool/topDonators`` API method

      Returns top miners by total donated amount (descending order).

      .. code-block:: python

         >>> top_donators = flexpoolapi.pool.top_donators()
         [<flexpoolapi.pool.TopDonator object 0xD7557BcC922E16D5248231Ee85919F5b01c97d12: 534.1283 ETH>, <flexpoolapi.pool.TopDonator object 0xD7557BcC922E16D5248231Ee85919F5b01c97d12: 277.7074 ETH>, ...]

         >>> top_donators[0]
         <flexpoolapi.pool.TopDonator object 0xD7557BcC922E16D5248231Ee85919F5b01c97d12: 534.1283 ETH>

         >>> top_donators[0].address
         0xD7557BcC922E16D5248231Ee85919F5b01c97d12
         >>> top_donators[0].pool_donation
         0.05
         >>> top_donators[0].total_donated
         534.128394767847103826
         >>> top_donators[0].first_joined
         datetime.datetime(2020, 5, 13, 20, 8, 7)

      **References:**

         :ref:`top_donator`

Blocks
------------------------------------------


.. py:method:: pool.last_blocks(count=10)

      - Wraps paged ``/pool/blocks`` API method

      Returns last N blocks mined by pool (descending order).

      .. code-block:: python

         >>> last_blocks = flexpoolapi.pool.last_blocks(5)
         [<flexpoolapi.shared.Block object Block #10208094 (0x4a916…0be99)>, <flexpoolapi.shared.Block object Uncle #10156606 (0x262bb…1134d)>, ...]


   **References:**

         :ref:`block`


.. py:method:: pool.blocks_paged(page: int)

      - Delegates to ``/pool/blocks`` API method

      Returns paged response wrapped into ``PageResponse`` class (descending order).

      .. hint::
            There are 10 blocks per one page

      .. code-block:: python

         >>> blocks_page_0 = flexpoolapi.pool.blocks_paged(page=0)  # Get first 10 blocks
         <flexpoolapi.shared.PageResponse object [<flexpoolapi.shared.Block object Block #10208094 (0x4a916…0be99)>, <flexpoolapi.shared.Block object Uncle #10156606 (0x262bb…1134d)>, <flexpoolapi.shared.Block object Block #9994360 (0x1251a…6dad9)>, ...]>
         >>> blocks_page_0.contents
         [<flexpoolapi.shared.Block object Block #10208094 (0x4a916…0be99)>, <flexpoolapi.shared.Block object Uncle #10156606 (0x262bb…1134d)>, <flexpoolapi.shared.Block object Block #9994360 (0x1251a…6dad9)>, ...]
         blocks_page_0.total_items
         528191
         >>> blocks_page_0.total_pages
         52820
         >> blocks_page_0.items_per_page
         10

      **References:**

         :ref:`page_response`

         :ref:`block`




Other
------------------------------------------

.. py:method:: pool.hashrate_chart()


   - Delegates to ``/pool/hashrateChart`` API Method

   Returns history of pool hashrate wrapped into ``flexpoolapi.pool.HashrateChartItem`` classes.

   **Example**

   .. code-block:: python

      [
         <flexpoolapi.pool.HashrateChartItem (T)>,
         <flexpoolapi.pool.HashrateChartItem (T - 10m)>,
         <flexpoolapi.pool.HashrateChartItem (T - 20m)>,
         <flexpoolapi.pool.HashrateChartItem (T - 30m)>,
         ...
      ]



   .. code-block:: python

         >>> hashrate_chart = flexpoolapi.pool.hashrate_chart()
         [<flexpoolapi.pool.HashrateChartItem object EU1 (21.7 TH/s), US1 (19.1 TH/s)>, <flexpoolapi.pool.HashrateChartItem object EU1 (21 TH/s), US1 (19.8 TH/s)>, ...]

         >>> hashrate_chart[0]
         <flexpoolapi.pool.HashrateChartItem object EU1 (21.8 TH/s), US1 (19.1 TH/s)>
         >>> hashrate_chart[0].servers
         {'EU1': 21818049812367, 'US1': 19274829582345}  # Pool's hashrate splitted by servers
         >>> hashrate_chart[0].total_hashrate
         41092879394712  # Total pool's hashrate
         >>> hashrate_chart[0].timestamp
         1592321400  # Chart item's Unix timestamp


   **References:**

      :ref:`hashrate_chart_item`

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


Miner Module
==========================================

.. py:class:: flexpoolapi.miner

    The API's ``Miner Module`` bindings.


Introduction
------------------------------------------

The API is wrapped into class for better interfacing.
First you need to initialize your miner class by calling ``miner = flexpoolapi.miner(<ADDRESS>)``, and then you would be able
to access the API.

.. code-block:: python

      >>> miner = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD")
      >>> effective, reported = miner.current_hashrate()
      >>> effective
      532256937
      >>> reported
      497730709

.. note::
      If the given address hasn't mined and doesn't exist in our database, the ``flexpoolapi.exceptions.MinerDoesNotExist`` exception would be risen.


Statistics
------------------------------------------

.. py:method:: miner.balance()

   - Delegates to ``/miner/<ADDRESS>/balance`` API Method

   Returns miner's unpaid balance in weis (minimal ETH unit)

   .. code-block:: python

         >>> flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").balance()
         575311819007598793  # 0.57 ETH

.. py:method:: miner.current_hashrate()

   - Delegates to ``/miner/<ADDRESS>/current`` API Method

   Returns miner's current hashrate in H/s (hashes per second).

   .. code-block:: python

         >>> effective, reported = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").current_hashrate()
         >>> effective
         532256937
         >>> reported
         497730709

.. py:method:: miner.daily_average_stats()

   - Delegates to ``/miner/<ADDRESS>/daily`` API Method

   Returns miner's daily average hashrate and the amount of shares submitted during the day.

   .. code-block:: python

         >>> stats = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").daily_average_stats()
         <flexpoolapi.shared.DailyAverageStats object 486.3 MH/s>
         >>> stats.effective_hashrate
         486282826.8471824
         >>> stats.reported_hashrate
         497730709.1734889
         >>> stats.valid_shares
         10503
         >>> stats.stale_shares
         58
         >> stats.invalid_shares
         0

**References:**

   :ref:`daily_average_stats`


.. py:method:: miner.stats()

   - Delegates to ``/miner/<ADDRESS>/stats`` API Method

   Returns miner's current and daily average hashrate, and the amount of shares submitted during the day.

   .. code-block:: python

         >>> stats = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").stats()
         <flexpoolapi.shared.Stats object 486.3 MH/s>
         >>> stats.current_effective_hashrate
         486282826.8471824
         >>> stats.average_effective_hashrate
         466831513.7732951
         >>> stats.current_reported_hashrate
         517639937.54042846
         >>> stats.average_reported_hashrate
         497730709.1734889
         >>> stats.valid_shares
         10503
         >>> stats.stale_shares
         58
         >> stats.invalid_shares
         0

**References:**

   :ref:`stats`

.. py:method:: miner.block_count()

   - Delegates to ``/miner/<ADDRESS>/blockCount`` API Method

   Returns the count of blocks mined by miner.

   .. code-block:: python

         >>> flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").block_count()
         2


.. py:method:: miner.details()

   - Delegates to ``/miner/<ADDRESS>/details`` API Method

   Returns the miner details.

   .. code-block:: python

         >>> details = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").details()
         <flexpoolapi.miner.MinerDetails object (0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD)>
         >>> details.min_payout_threshold
         200000000000000000  # 0.2 ETH
         >>> details.pool_donation
         0.02
         >>> details.first_joined_date
         datetime.datetime(2020, 4, 30, 20, 50)
         >>> details.censored_email
         'mai*@exa****.com'
         >>> details.censored_ip
         '*.*.*.1'

**References:**

   :ref:`miner_details`

Payments
------------------------------------------

.. py:method:: miner.payment_count()

   - Delegates to ``/miner/<ADDRESS>/paymentCount`` API Method

   Returns the amount of payments done.

   .. code-block:: python

         >>> stats = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").payment_count()
         47

.. py:method:: miner.payments_paged(page: int)

      - Delegates to ``/miner/<ADDRESS>/payments`` API method

      Returns paged response wrapped into ``PagedResponse`` class (descending order, latest first).

      .. hint::
            There are 10 payments per one page.

      .. code-block:: python

         >>> payments_page_0 = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").payments_paged(page=0)
         <flexpoolapi.shared.PageResponse object [<flexpoolapi.miner.Transaction object  1.61075 ETH (2020 Jun 06 14:12)>, <flexpoolapi.miner.Transaction object  1.38525 ETH (2020 May 30 00:20)>, ...]>
         >>> blocks_page_0.contents
         [<flexpoolapi.miner.Transaction object  1.61075 ETH (2020 Jun 06 14:12)>, <flexpoolapi.miner.Transaction object  1.38525 ETH (2020 May 30 00:20)>, ...]
         blocks_page_0.total_items
         47
         >>> blocks_page_0.total_pages
         5
         >> blocks_page_0.items_per_page
         10


**References:**

   :ref:`page_response`

   :ref:`transaction`


Blocks
------------------------------------------

.. py:method:: miner.blocks_paged(page: int)

      - Delegates to ``/miner/<ADDRESS>/blocks`` API method

      Returns paged response wrapped into ``PagedResponse`` class (descending order, latest first).

      .. hint::
            There are 10 blocks per one page

      .. code-block:: python

         >>> payments_page_0 = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").blocks_paged(page=0)
         <flexpoolapi.shared.PageResponse object [<flexpoolapi.shared.Block object Uncle #10156606 (0x262bb…1134d)>, <flexpoolapi.shared.Block object Block #9994360 (0x1251a…6dad9)>, ...]>
         >>> blocks_page_0.contents
         [<flexpoolapi.shared.Block object Uncle #10156606 (0x262bb…1134d)>, <flexpoolapi.shared.Block object Block #9994360 (0x1251a…6dad9)>]]
         blocks_page_0.total_items
         2
         >>> blocks_page_0.total_pages
         1
         >> blocks_page_0.items_per_page
         10


**References:**

   :ref:`page_response`

   :ref:`block`



Other
------------------------------------------

.. py:method:: miner.chart()


   - Delegates to ``/miner/<ADDRESS>/chart`` API Method

   Returns history of miner hashrate and shares wrapped into ``flexpoolapi.shared.StatChartItem`` classes.

   **Example**

   .. code-block:: python

      [
         <flexpoolapi.shared.StatChartItem (T)>,
         <flexpoolapi.shared.StatChartItem (T - 10m)>,
         <flexpoolapi.shared.StatChartItem (T - 20m)>,
         <flexpoolapi.shared.StatChartItem (T - 30m)>,
         ...
      ]



   .. code-block:: python

         >>> chart = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").chart()
         [<flexpoolapi.shared.StatChartItem object (2020 Jun 17 12:40)>, <flexpoolapi.shared.StatChartItem object (2020 Jun 17 12:30)>, ...]

         >>> chart[0]
         <flexpoolapi.shared.StatChartItem object (2020 Jun 17 12:40)>
         >>> hashrate_chart[0].effective
         497730709
         >>> hashrate_chart[0].reported
         532256937
         >>> hashrate_chart[0].valid_shares
         72
         >>> hashrate_chart[0].stale_shares
         1
         >>> hashrate_chart[0].invalid_shares
         0


**References:**

   :ref:`stat_chart_item`




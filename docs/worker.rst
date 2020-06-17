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


Worker Module
==========================================

.. py:class:: flexpoolapi.worker

    The API's ``Worker Module`` bindings.


Introduction
------------------------------------------

As py-flexpoolapi is coded in Pythonic Style, there's no such thing as Worker API by itself.
Instead, the worker API is mounted into the Miner module.

.. code-block:: python

      >>> miner = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD")
      >>> workers = miner.workers()
      [<flexpoolapi.worker.Worker object rig1 (0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD)>, <flexpoolapi.worker.Worker object rig2 (0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD)>, ...]
      >>> workers[0].worker_name
      'rig1'
      >>> workers[0].is_online
      True
      >>> workers[0].last_seen_date
      time.datetime(2020, 6, 17, 12, 13, 25)


.. warning::
        The ``flexpoolapi.worker.Worker`` class is intended to be initialized ONLY by ``miner.workers()``.



Statistics
------------------------------------------

.. py:method:: worker.current_hashrate(page: int)

      - Delegates to ``/worker/<MINER_ADDRESS>/<WORKER_NAME>/current`` API method

      Returns worker's current hashrate.

      .. code-block:: python

         >>> worker = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").workers()[0]
         <flexpoolapi.worker.Worker object rig1 (0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD)>
         >>> effective, reported = worker.current_hashrate()
         >>> effective
         164963909  # 165 MH/s
         >>> reported
         196102107  # 196.1 MH/s


.. py:method:: worker.daily_average_stats()

   - Delegates to ``/woker/<MINER_ADDRESS>/<WORKER_NAME>/daily`` API Method

   Returns workers's daily average hashrate and the amount of shares submitted during the day. Same as ``miner.daily_average_stats()``

   .. code-block:: python

         >>> stats = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").workers()[0].daily_average_stats()
         <flexpoolapi.shared.DailyAverageStats object 121.6 MH/s>
         >>> stats.effective_hashrate
         121570706.7117956
         >>> stats.reported_hashrate
         124432677.29337223
         >>> stats.valid_shares
         2625
         >>> stats.stale_shares
         12
         >> stats.invalid_shares
         0

   ``flexpoolapi.shared.DailyAverageStats`` reference: <TODO/TBD>


.. py:method:: worker.stats()

   - Delegates to ``/worker/<MINER_ADDRESS>/<WORKER_NAME>/stats`` API Method

   Returns workers's current and daily average hashrate, and the amount of shares submitted during the day. Same as ``miner.stats()``

   .. code-block:: python

         >>> stats = flexpoolapi.miner("0xa598f8fB0a44eF74357815e318dC1C48719Fc3AD").workers()[0].stats()
         <flexpoolapi.shared.Stats object 121.6 MH/s>
         >>> stats.current_effective_hashrate
         121592946.2467181
         >>> stats.average_effective_hashrate
         121570706.7117956
         >>> stats.current_reported_hashrate
         128733972.73389934
         >>> stats.average_reported_hashrate
         124432677.29337223
         >>> stats.valid_shares
         2625
         >>> stats.stale_shares
         12
         >> stats.invalid_shares
         0

   ``flexpoolapi.shared.Stats`` reference: <TODO/TBD>


Other
------

.. py:method:: worker.chart()


   - Delegates to ``/worker/<MINER_ADDRESS>/<WORKER_NAME>/chart`` API Method

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
         124432677
         >>> hashrate_chart[0].reported
         133064234
         >>> hashrate_chart[0].valid_shares
         15
         >>> hashrate_chart[0].stale_shares
         1
         >>> hashrate_chart[0].invalid_shares
         0


   ``flexpoolapi.shared.StatChartItem`` reference: <TODO/TBD>

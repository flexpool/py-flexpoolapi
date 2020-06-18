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


Quickstart
==========================================

**py-flexpoolapi** is a pythonic library for easy interfacing with Flexpool Public API.
The library has minimal dependencies which means it can be easy used inside every environment.

Installation
------------------------------------------

The recommended way is to install our PyPI package using **pip**.

.. code-block:: bash

        pip3 install flexpoolapi


.. note::

        You need to use ``pip`` instead of ``pip3`` if you're using Windows.


However, you can always build it from source by

.. code-block:: bash

   git clone https://github.com/flexpool/py-flexpoolapi
   cd py-flexpoolapi
   make install


Usage
------------------------------------------

Great! The **py-flexpoolapi** is installed successfully, you can check if it works by

.. code-block:: python

      >>> import flexpoolapi
      >>> flexpoolapi.pool.hashrate()
      {'EU1': 21818049812367, 'US1': 19274829582345, 'total': 41092879394712}


Quick example
-------------------------------------------

.. code-block:: python

      >>> import flexpoolapi

      # Pool
      >>> flexpoolapi.pool.hashrate()
      {'EU1': 21818049812367, 'US1': 19274829582345, 'total': 41092879394712}
      >>> flexpoolapi.pool.miners_online()
      47192
      >>> flexpoolapi.pool.workers_online()
      253194

      # Miner
      >>> miner = flexpoolapi.miner("0x8B82eE62Ae306BF1bE085458a08241759d1d7E20")
      >>> miner.balance()
      575311819007598793
      >>> effective_hashrate, reported_hashrate = miner.current_hashrate()
      (532256937, 497730709)

For better understanding, we recommend reading the documentation fully.
If you don't like reading documentation, you can always refer to the `Examples Directory on GitHub <https://github.com/flexpool/py-flexpoolapi/tree/master/examples>`_.
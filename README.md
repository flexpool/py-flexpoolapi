# py-flexpoolapi

[![PyPI Latest Release](https://img.shields.io/pypi/v/flexpoolapi.svg)](https://pypi.org/project/flexpoolapi)
![Tests](https://github.com/flexpool/py-flexpoolapi/workflows/Tests/badge.svg)
![Upload Python Package](https://github.com/flexpool/py-flexpoolapi/workflows/Upload%20Python%20Package/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/py-flexpoolapi/badge/?version=latest)](https://py-flexpoolapi.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/flexpool/py-flexpoolapi/badge.svg?branch=master)](https://coveralls.io/github/flexpool/py-flexpoolapi?branch=master) [![Join the chat at https://gitter.im/flexpool/py-flexpoolapi](https://badges.gitter.im/flexpool/py-flexpoolapi.svg)](https://gitter.im/flexpool/py-flexpoolapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Structured Python wrapper for Flexpool API.

[Documentation](https://py-flexpoolapi.readthedocs.io)

# Installation

Install **py-flexpoolapi**.

## Using pip
```sh
pip3 install flexpoolapi
```

## Build from source
```sh
git clone https://github.com/flexpool/py-flexpoolapi.git
cd py-flexpoolapi
pip3 install -r requirements.txt
make install  # or `python3 setup.py install`
```

# Usage

Quick example:
```python
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

```

For better understanding, we recommend reading the [documentation](https://py-flexpoolapi.readthedocs.io). If you don't like reading documentation, you can always refer to the [examples directory](https://github.com/flexpool/py-flexpoolapi/tree/master/examples).

# License
MIT

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

from flask import Flask, make_response, request
import math

from . import simdata
from . import simutils


def api_pool_hashrate():
    resp = make_response(simutils.wrap_response({"EU1": simdata.POOL_HASHRATE_EU1,
                                                 "US1": simdata.POOL_HASHRATE_US1,
                                                 "total": simdata.POOL_HASHRATE_EU1 + simdata.POOL_HASHRATE_US1}))

    resp.mimetype = "application/json"
    return resp


def api_pool_hashrate_chart():
    resp = make_response(simutils.wrap_response(simdata.POOL_HASHRATE_CHART))
    resp.mimetype = "application/json"
    return resp


def api_pool_miners_online():
    resp = make_response(simutils.wrap_response(simdata.MINERS_ONLINE))
    resp.mimetype = "application/json"
    return resp


def api_pool_workers_online():
    resp = make_response(simutils.wrap_response(simdata.WORKERS_ONLINE))
    resp.mimetype = "application/json"
    return resp


def api_pool_block_count():
    resp = make_response(simutils.wrap_response(simdata.NUM_BLOCKS))
    resp.mimetype = "application/json"
    return resp


def api_pool_blocks():
    page = int(request.args.get("page"))
    resp = make_response(simutils.wrap_response({
        "data": simdata.BLOCKS[page*10:(page+1)*10],
        "total_pages": math.ceil(simdata.NUM_BLOCKS / 10),
        "total_items": simdata.NUM_BLOCKS,
        "items_per_page": 10
    }))
    resp.mimetype = "application/json"
    return resp


def api_pool_top_miners():
    resp = make_response(simutils.wrap_response(simdata.TOP_MINERS))
    resp.mimetype = "application/json"
    return resp


def api_pool_top_donators():
    resp = make_response(simutils.wrap_response(simdata.TOP_DONATORS))
    resp.mimetype = "application/json"
    return resp


def api_pool_avg_luck_roundtime():
    resp = make_response(simutils.wrap_response({"luck": simdata.AVG_LUCK, "round_time": simdata.AVG_ROUNDTIME}))
    resp.mimetype = "application/json"
    return resp


def api_miner_exists(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(True))

    resp.mimetype = "application/json"
    return resp


def api_miner_balance(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.MINER_BALANCE))

    resp.mimetype = "application/json"
    return resp


def api_miner_current_hashrate(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response({
        "effective_hashrate": simdata.CURRENT_EFFECTIVE_HASHRATE,
        "reported_hashrate": simdata.CURRENT_REPORTED_HASHRATE
    }))

    resp.mimetype = "application/json"
    return resp


def api_miner_daily(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response({
        "effective_hashrate": simdata.DAILY_EFFECTIVE_HASHRATE,
        "reported_hashrate": simdata.DAILY_REPORTED_HASHRATE,
        "valid_shares": simdata.DAILY_VALID_SHARES,
        "stale_shares": simdata.DAILY_STALE_SHARES,
        "invalid_shares": simdata.DAILY_INVALID_SHARES
    }))

    resp.mimetype = "application/json"
    return resp


def api_miner_stats(miner):
    assert miner == simdata.MINER_ADDRESS
    daily = {
        "effective_hashrate": simdata.DAILY_EFFECTIVE_HASHRATE,
        "reported_hashrate": simdata.DAILY_REPORTED_HASHRATE,
        "valid_shares": simdata.DAILY_VALID_SHARES,
        "stale_shares": simdata.DAILY_STALE_SHARES,
        "invalid_shares": simdata.DAILY_INVALID_SHARES
    }
    current = {
        "effective_hashrate": simdata.CURRENT_EFFECTIVE_HASHRATE,
        "reported_hashrate": simdata.CURRENT_REPORTED_HASHRATE
    }
    resp = make_response(simutils.wrap_response({"current": current, "daily": daily}))

    resp.mimetype = "application/json"
    return resp


def api_miner_worker_count(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.WORKER_COUNT))

    resp.mimetype = "application/json"
    return resp


def api_miner_workers(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.WORKERS))

    resp.mimetype = "application/json"
    return resp


def api_miner_chart(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.MINER_CHART))

    resp.mimetype = "application/json"
    return resp


def api_miner_payment_count(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.PAYMENT_COUNT))

    resp.mimetype = "application/json"
    return resp


def api_miner_payments(miner):
    assert miner == simdata.MINER_ADDRESS
    page = int(request.args.get("page"))
    resp = make_response(simutils.wrap_response({
        "data": simdata.PAYMENTS[page*10:(page+1)*10],
        "total_pages": math.ceil(simdata.PAYMENT_COUNT / 10),
        "total_items": simdata.PAYMENT_COUNT,
        "items_per_page": 10
    }))
    resp.mimetype = "application/json"
    return resp


def api_miner_block_count(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response(simdata.MINER_BLOCK_COUNT))

    resp.mimetype = "application/json"
    return resp


def api_miner_blocks(miner):
    assert miner == simdata.MINER_ADDRESS
    page = int(request.args.get("page"))
    resp = make_response(simutils.wrap_response({
        "data": simdata.MINER_BLOCKS[page*10:(page+1)*10],
        "total_pages": math.ceil(simdata.MINER_BLOCK_COUNT / 10),
        "total_items": simdata.MINER_BLOCK_COUNT,
        "items_per_page": 10
    }))
    resp.mimetype = "application/json"
    return resp


def api_miner_details(miner):
    assert miner == simdata.MINER_ADDRESS
    resp = make_response(simutils.wrap_response({
        "min_payout_threshold": simdata.MINER_MIN_PAYOUT_THRESHOLD,
        "pool_donation": simdata.MINER_POOL_DONATION,
        "censored_email": simdata.MINER_CENSORED_EMAIL,
        "censored_ip": simdata.MINER_CENSORED_IP,
        "first_joined": simdata.MINER_FIRST_JOINED
    }))
    resp.mimetype = "application/json"
    return resp


def api_worker_current(miner, worker):
    assert miner == simdata.MINER_ADDRESS
    assert worker in simdata.WORKERS_MAP
    resp = make_response(simutils.wrap_response({
        "effective_hashrate": simdata.WORKERS_MAP[worker]["effective_hashrate"],
        "reported_hashrate": simdata.WORKERS_MAP[worker]["reported_hashrate"]
    }))

    resp.mimetype = "application/json"
    return resp


def api_worker_daily(miner, worker):
    assert miner == simdata.MINER_ADDRESS
    assert worker in simdata.WORKERS_MAP
    resp = make_response(simutils.wrap_response({
        "effective_hashrate": simdata.WORKERS_MAP[worker]["daily_effective_hashrate"],
        "reported_hashrate": simdata.WORKERS_MAP[worker]["daily_reported_hashrate"],
        "valid_shares": simdata.WORKERS_MAP[worker]["valid_shares"],
        "stale_shares": simdata.WORKERS_MAP[worker]["stale_shares"],
        "invalid_shares": simdata.WORKERS_MAP[worker]["invalid_shares"]
    }))

    resp.mimetype = "application/json"
    return resp


def api_worker_stats(miner, worker):
    assert miner == simdata.MINER_ADDRESS
    assert worker in simdata.WORKERS_MAP
    daily = {
        "effective_hashrate": simdata.WORKERS_MAP[worker]["daily_effective_hashrate"],
        "reported_hashrate": simdata.WORKERS_MAP[worker]["daily_reported_hashrate"],
        "valid_shares": simdata.WORKERS_MAP[worker]["valid_shares"],
        "stale_shares": simdata.WORKERS_MAP[worker]["stale_shares"],
        "invalid_shares": simdata.WORKERS_MAP[worker]["invalid_shares"]
    }

    current = {
        "effective_hashrate": simdata.WORKERS_MAP[worker]["effective_hashrate"],
        "reported_hashrate": simdata.WORKERS_MAP[worker]["reported_hashrate"]
    }

    resp = make_response(simutils.wrap_response({"current": current, "daily": daily}))

    resp.mimetype = "application/json"
    return resp


def api_worker_chart(miner, worker):
    assert miner == simdata.MINER_ADDRESS
    assert worker in simdata.WORKERS_MAP
    resp = make_response(simutils.wrap_response(simdata.WORKERS_CHART_MAP[worker]))

    resp.mimetype = "application/json"
    return resp


def prepare_api_app():
    app = Flask("Flexpool API Simulation")

    # Pool API
    app.route("/api/v1/pool/hashrate")(api_pool_hashrate)
    app.route("/api/v1/pool/hashrateChart")(api_pool_hashrate_chart)
    app.route("/api/v1/pool/minersOnline")(api_pool_miners_online)
    app.route("/api/v1/pool/workersOnline")(api_pool_workers_online)
    app.route("/api/v1/pool/blockCount")(api_pool_block_count)
    app.route("/api/v1/pool/blocks")(api_pool_blocks)
    app.route("/api/v1/pool/topMiners")(api_pool_top_miners)
    app.route("/api/v1/pool/topDonators")(api_pool_top_donators)
    app.route("/api/v1/pool/avgLuckRoundtime")(api_pool_avg_luck_roundtime)

    # Miner API
    app.route("/api/v1/miner/<miner>/exists")(api_miner_exists)
    app.route("/api/v1/miner/<miner>/balance")(api_miner_balance)
    app.route("/api/v1/miner/<miner>/current")(api_miner_current_hashrate)
    app.route("/api/v1/miner/<miner>/daily")(api_miner_daily)
    app.route("/api/v1/miner/<miner>/stats")(api_miner_stats)
    app.route("/api/v1/miner/<miner>/workerCount")(api_miner_worker_count)
    app.route("/api/v1/miner/<miner>/workers")(api_miner_workers)
    app.route("/api/v1/miner/<miner>/chart")(api_miner_chart)
    app.route("/api/v1/miner/<miner>/paymentCount")(api_miner_payment_count)
    app.route("/api/v1/miner/<miner>/payments")(api_miner_payments)
    app.route("/api/v1/miner/<miner>/blockCount")(api_miner_block_count)
    app.route("/api/v1/miner/<miner>/blocks")(api_miner_blocks)
    app.route("/api/v1/miner/<miner>/details")(api_miner_details)

    # Worker API
    app.route("/api/v1/worker/<miner>/<worker>/current")(api_worker_current)
    app.route("/api/v1/worker/<miner>/<worker>/daily")(api_worker_daily)
    app.route("/api/v1/worker/<miner>/<worker>/stats")(api_worker_stats)
    app.route("/api/v1/worker/<miner>/<worker>/chart")(api_worker_chart)

    return app



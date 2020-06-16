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

import json
import threading
import requests
import time


def selftest_api_method():
    return "1"


class APISimulator:
    def __init__(self, app):
        self.app = app
        self.thread = None
        app.route("/selftest")(selftest_api_method)

    def start(self):
        self.thread = StoppableThread(target=self.app.run, daemon=True)
        self.thread.start()
        while True:
            try:
                if requests.get("http://localhost:5000/selftest").text == "1":
                    break
            except requests.ConnectionError:
                pass
            time.sleep(1)

    def stop(self):
        self.thread.stop()


class StoppableThread(threading.Thread):
    # https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def wrap_response(data):
    return json.dumps({"result": data, "error": None})

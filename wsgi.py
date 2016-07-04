#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    Scryb WSGI
    ~~~~~~~~~~

    :license: MIT license. See LICENSE file.
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from scryb import frontend


frontend_app = frontend.create_app()


if __name__ == '__main__':
    run_simple(
        frontend_app.config.get('HOST', 'localhost'),
        frontend_app.config.get('PORT', 5000),
        frontend_app,
        use_debugger=frontend_app.config.get('DEBUG'),
        use_reloader=frontend_app.config.get('DEBUG'),
    )

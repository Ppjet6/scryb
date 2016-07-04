#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    Scryb WSGI
    ~~~~~~~~~~

    :license: MIT license. See LICENSE file.
"""

from werkzeug.serving import run_simple
from scryb import frontend


frontend_app = frontend.create_app(settings_override={
    'DEBUG': True,
    'DEV': True,
    'SECRET_KEY': 'secret passphrase',
})


if __name__ == '__main__':
    run_simple('localhost', 5000, frontend_app,
        use_debugger=frontend_app.config.get('DEBUG'),
        use_reloader=frontend_app.config.get('DEBUG'),
    )

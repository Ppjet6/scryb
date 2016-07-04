#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    Scryb frontend
    ~~~~~~~~~~~~~~

    :license: MIT license. See LICENSE file.
"""

from flask import Blueprint


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return 'Hello World'

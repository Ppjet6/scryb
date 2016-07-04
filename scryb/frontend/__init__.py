#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    Scryb frontend
    ~~~~~~~~~~~~~~

    :license: MIT license. See LICENSE file.
"""

from .. import factory


def create_app(settings_override=None):
    return factory.create_app(__name__, __path__, settings_override)

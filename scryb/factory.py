#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
    Scryb
    ~~~~~

    :license: MIT license. See LICENSE file.
"""

from os import getenv
from flask import Flask

from .helpers import register_blueprints


def create_app(package_name, package_path, settings_override=None):
    """Return a :class:`Flask` application instance configured.

    :param package_name: the package name
    :param package_path: the package path
    :param settings_override: a dictionary of settings to override
    """

    app = Flask(package_name)
    app.config.from_object(settings_override)

    register_blueprints(app, package_name, package_path)

    return app

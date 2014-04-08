# -*- coding: utf-8 -*-
"""Setup the placeholder application"""
from __future__ import print_function

from placeholder import model
from tgext.pluggable import app_model

def bootstrap(command, conf, vars):
    print('Bootstrapping placeholder...')
# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _, lazy_ugettext as l_

from placeholder import model
from placeholder.model import DBSession

class RootController(TGController):
    @expose('placeholder.templates.index')
    def index(self):
        sample = DBSession.query(model.Sample).first()
        return dict(sample=sample)

# -*- coding: utf-8 -*-
"""
Copyright © 2000 Puria Nafisi Azizi <puria.nafisi@axant.it>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.
"""


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from collections import namedtuple
import os
import requests
import tg

from PIL import ImageFont
from io import BytesIO
from tg import TGController, expose
from PIL import Image, ImageDraw, ImageColor
import urllib


FONT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'Marlboro.ttf')

class RootController(TGController):
    @expose(content_type="image/png")
    def _default(self, size, text=None, bgcolor="DDD", color="888", format='PNG', font_size=None, **kwargs):
        size = self._parse_size(size)
        bgcolor, color = self._parse_colors(bgcolor, color)
        image = Image.new('RGB', size, bgcolor)
        draw = ImageDraw.Draw(image)
        text = text if text else "%s x %s" % size
        calculated_font_size = ((size.width - 10) / len(text)) * 2
        font_size = font_size if font_size else calculated_font_size
        try:
            font = ImageFont.truetype(FONT_PATH, font_size)
        except IOError:
            font = ImageFont.load_default()
        text_size = font.getsize(text)
        text_center = (size.width / 2 - text_size[0] / 2,
                       size.height / 2 - text_size[1] / 2)
        draw.text(text_center, text.decode('utf-8'), fill=color, font=font)
        fp = StringIO.StringIO()
        image.save(fp, format)

        return fp.getvalue()

    def _parse_size(self, size):
        Size = namedtuple('Size', ['width', 'height'])
        try:
            width, height = size.split('x')
        except ValueError:
            width = height = size

        try:
            size = Size(int(width), int(height))
        except ValueError:
            size = Size(1, 1)

        return size

    def _parse_colors(self, bgcolor, color):
        try:
            bgcolor = ImageColor.getrgb(bgcolor)
        except ValueError:
            try:
                bgcolor = ImageColor.getrgb('#%s' % bgcolor)
            except ValueError:
                bgcolor = ImageColor.getrgb('#DDD')

        try:
            color = ImageColor.getrgb(color)
        except ValueError:
            try:
                color = ImageColor.getrgb('#%s' % color)
            except ValueError:
                color = ImageColor.getrgb('#888')
        return bgcolor, color

    @expose(content_type="image/png")
    def stevenseagal(self, size):
        return self._get_hero_image('http://www.stevensegallery.com', size)

    @expose(content_type="image/png")
    def nicolascage(self, mode='', size='200x200'):
        if mode not in ['c', 'g', 'gif']:
            size = mode
            mode = None
        base = 'http://www.placecage.com/'
        if mode:
            base += '%s/' % mode
        return self._get_hero_image(base, size)

    @expose(content_type="image/png")
    def billmurray(self, size):
        return self._get_hero_image('http://www.fillmurray.com', size)

    def _get_hero_image(self, url, size):
        size = self._parse_size(size)
        response = requests.get('%s/%s/%s' % (url, size.width, size.height))
        img = Image.open(BytesIO(response.content))

        fp = StringIO.StringIO()
        img.save(fp, 'PNG')
        return fp.getvalue()

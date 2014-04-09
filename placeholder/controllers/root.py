# -*- coding: utf-8 -*-
"""Main Controller"""

import StringIO
from collections import namedtuple
import os

from PIL import ImageFont
from tg import TGController, expose
from PIL import Image, ImageDraw, ImageColor


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
# -*- coding: utf-8 -*-
"""Main Controller"""

import StringIO
from collections import namedtuple
import os

from PIL import ImageFont
from tg import TGController, expose
from PIL import Image, ImageDraw


FONT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'Marlboro.ttf')

class RootController(TGController):
    @expose(content_type="image/png")
    def _default(self, size_s, text=None, bgcolor="DDD", color="888", **kwargs):
        Size = namedtuple('Size', ['width', 'height'])

        try:
            width, height = size_s.split('x')
        except ValueError:
            width = height = size_s

        try:
            size = Size(int(width), int(height))
        except ValueError:
            size = Size(1, 1)

        image = Image.new('RGB', size)
        draw = ImageDraw.Draw(image)
        draw.rectangle([(0, 0), size], fill='#' + bgcolor)
        center = (size.width / 2, size.height / 2)

        if not text:
            text = "%s x %s" % size

        print_area = size.width - 10
        text_size = (print_area / len(text)) * 2
        font = ImageFont.truetype(FONT_PATH, text_size)


        text_size = font.getsize(text)
        text_center = (center[0] - text_size[0] / 2,
                       center[1] - text_size[1] / 2)

        draw.text(text_center, text.decode('utf-8'), fill='#%s' % color, font=font)

        fp = StringIO.StringIO()
        image.save(fp, 'PNG')

        return fp.getvalue()


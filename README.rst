About placeholder
-------------------------

tgapp-placeholder is a Pluggable application for TurboGears2 that allows placeholder images generation on the fly.
Inspired by http://dummyimage.com/ and https://github.com/darkrho/django-dummyimage.

Installing
-------------------------------

placeholder can be installed both from pypi or from github::

    pip install tgapp-placeholder

should just work for most of the users

Plugging placeholder
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with placeholder::

    plug(base_config, 'placeholder')

You will be able to access the plugged application at
*http://localhost:8080/placeholder*.

Using placeholder
-----------------

You are now able to get your fake images by calling::

  http://you-application/placeholder/{width} #for a square image
  http://you-application/placeholder/{width}x{height}
  http://you-application/placeholder/{width}x{height}?text={some text value}

actually the parameters you can play with are:
    * `text` : a custom online text wich size is calculated to fit your image width
    * `bgcolor` : the background color in HEX rgb form (default set to 'DDDDDD')
    * `color` : the text color in HEX rgb form (default set to '888888')
    * `format` : available formats available `here <http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html>` (default set to PNG)
    * `font_size` : font_size of the eventtual text. If none is provided it is automagically calculated to fit the whole text in the image width.

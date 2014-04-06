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

Available Hooks
----------------------

placeholder makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

placeholder exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:


django-cors
===========

A Django app for handling Cross-Origin Resource Sharing.

Install by cloning the repo and running

::

    sudo python setup.py install

Then add the app to the installed apps in your settings file::

    INSTALLED_APPS = (
        # ...
        'cors',
        # ...
    )

To allow requests to be made from the browser from any domain, use ``AllowOriginMiddleware``::

    MIDDLEWARE_CLASSES = (
        # ...
        'cors.middleware.AllowOriginMiddleware',
        # ...
    )

Customisation
-------------

In some cases you may need to override the list of allowed Headers. By specifying the setting
``CORS_ALLOW_HEADERS`` you can set the list. By default the setting is `Content-Type, Authorization`.

If you specify this setting, the setting is *NOT* additive but a replacement.

i.e.::

    CORS_ALLOW_HEADERS = 'Authorization'

Will only return the header `Authorization`

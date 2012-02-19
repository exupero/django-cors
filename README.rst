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

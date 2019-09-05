import warnings
from flask import Flask
from flask import current_app
from redis import Redis


class RedisClient(object):

    def __init__(self, app=None, **kwargs):
        self._redisclient = None
        self.redis_class = Redis
        self.redis_kwargs = kwargs

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not app or not isinstance(app, Flask):
            raise Exception('Invalid Flask application instance')

        if 'REDIS_URL' not in app.config:
            warnings.warn(
                'No REDIS_URL is set '
                'Defaulting REDIS_URL to "redis://localhost:6379/0"'
            )

            app.config.setdefault('REDIS_URL', 'redis://localhost:6379/0')

        redis_url = app.config.get('REDIS_URL')
        kwargs = self.redis_kwargs
        self._redisclient = self.redis_class.from_url(redis_url, **kwargs)

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["redisclient"] = self._redisclient

    @property
    def connection(self):
        assert 'redisclient' in current_app.extensions
        return current_app.extensions['redisclient']

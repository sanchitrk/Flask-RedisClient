# Flask-RedisClient
This is a simple Flask extension that allows you to use Redis in your application.

## Installation & Basic Configuration
```shell script
$ (venv) pip install Flask-RedisClient
```
Configure it within your Flask config
```python
REDIS_URL = "redis://:password@localhost:6379/0"
```

## Usage
Add Redis Client to your application
```python
from flask import Flask
from flask_redisclient import RedisClient

app = Flask(__name__)
redis_client = RedisClient(app)
```

or if you are using app factory pattern

```python
redis_client = RedisClient()
def create_app():
    app = Flask(__name__)
    redis_client.init_app(app)
    return app
```

### Accessing Redis Client
The `redis_client.connection` returns a regular `Redis` instance from the [`redis-py`](https://github.com/andymccurdy/redis-py) package.

You can use all the methods and features available in [`redis-py`](https://redis-py.readthedocs.io/en/latest/) package.
```python
from app import redis_client

@app.route('/')
def index():
    redis_conn = redis_client.connection
    return redis_conn.get('world')
```

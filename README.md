Flask-NPM
=========
Flask-NPM is a Flask extension which makes it easy to
serve static files from node_modules

## Installation ##

### PyPI ###

Flask-NPM is available on PyPI! You can install it with pip.

```sh
pip install Flask-NPM
```

### Manual ###

If you want to do it the hard way you can clone the repository and
install Flask-NPM in a virtualenv. 

1. Clone it `git clone https://github.com/lightsing/Flask-NPM.git`
2. Enter it `cd Flask-NPM`
3. Create a virtualenv and enter it (Optional) `virtualenv venv && source venv/bin/activate`
4. Install it `python setup.py install`

## Instructions ##

After Flask-NPM is installed you will be able to import the `flask.ext.NPM`
packages. There is only one thing you care about inside the package
which is the `NPM` class.

```python
from flask.ext.NPM import NPM
```

There are two ways to use the `NPM` class.

1. Add the application object at construction time

```python
app = Flask(__name__)
NPM(app)
```

2. Or initialize the application with `NPM.init_app`

```python
NPM = NPM()
app = Flask(__name__)
NPM.init_app(app)
```

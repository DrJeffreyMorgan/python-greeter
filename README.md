# python-greeter

![Travis (.org)](https://img.shields.io/travis/DrJeffreyMorgan/python-greeter.svg)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

A simple Python package that combines unit testing and continuous integration.

## Install

```bash
pip install git+https://github.com/DrJeffreyMorgan/python-greeter.git
```

## Use

```python
from greeter import Greeter

hello_world = Greeter('World!')
print(hello_world.greet())
```

## Test

```bash
PYTHONPATH=greeter python tests/test_greet.py
```

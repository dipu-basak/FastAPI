# Day 2: Basics
- type hints


## Details

### Type Hints
[codes here](../day_02/type_hint.ipynb)

Type Hints (type annotations) are just the variable types.
In other languages like c, when declaring a variable, using data type is mandatory. but not in python. For example in c, you have to write `int n = 50;`. but in python you can just use `n = 50` and be done with it.

But, though it is not mandatory, data types can be declared in python too by following syntax
````python
n: int
# or in functions
def func(a: int, s: str):
    print(str(a) + s)
# this function will concatinate a and s
````
But why tyoe hint is needed now? well, by giving the interpreter `hint` aboubt the data type, the `IDE` can help us call the methods ( everything in python is `object`, remember?) or autocomplets parts of code. Read more [here](https://fastapi.tiangolo.com/python-types/).

### `typing` module
For some cases,`` typing module`` will be needed, for example when we want to declare that something has "any type", we can use Any from typing:


````python
from typing import Any

def some_function(data: Any):
    print(data)    
````
### Union
Lets say a variable can be both `int` or `str`. we can use union(`|`)
````python
def func(a: int| str):
    print(type(a))
````
types can be `None` (equivalent of `NULL` in other languages) too.

```python
def func(name: str | None = None):
    if name is not None:
        print(f"Hello, {name}")
    else:
        print("hello world")
```
This means a can be either an int or None. we can also use the older Optional syntax:
```python
# usnig typing
import typing

def func(name: typing.Optional[str] = None):
  if name is not None:
        print(f"Hello, {name}")
  else:
      print("hello world")

func()
```
### list
````python
def func(items: list[str]):
  for item in items:
    print(item.capitalize())

func(['hi', 'hello', 'bye'])
````

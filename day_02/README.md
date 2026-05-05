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

### Additional Examples from Notebook

These are executable code blocks from `type_hint.ipynb` that provide practical demonstrations and variations not fully covered above.

1. **Basic Type Hints with Function Execution**  
   Demonstrates basic type hints for a variable and a function, including a function call that concatenates an integer (converted to string) with a title-cased string.
   ```python
   n: int
   def f(a: int, s: str):
     print(str(a) + s.title())
   f(3, 'hiii')
   ```

2. **Using `typing.Any` with a String Input**  
   Illustrates `typing.Any` for flexible data types, called with a string to show type printing.
   ```python
   import typing
   
   def some_function(data: typing.Any):
     print(type(data))
   some_function('hii')
   ```

3. **Using `typing.Any` with an Integer Input**  
   Same as above, but with an integer input to demonstrate handling different types.
   ```python
   import typing
   
   def some_function(data: typing.Any):
     print(type(data))
   some_function(10)
   ```

4. **Union with `None` and Function Call with Argument**  
   Shows union type with `None`, called with an argument to trigger the personalized greeting.
   ```python
   def func(name: str | None = None):
       if name is not None:
           print(f"Hello, {name}")
       else:
         print("hello world")
   
   func('Basak')
   ```

5. **Union with `None` and Function Call Without Argument**  
   Same function, called without arguments to use the default `None` and print the fallback message.
   ```python
   def func(name: str | None = None):
       if name is not None:
           print(f"Hello, {name}")
       else:
         print("hello world")
   
   func()
   ```

6. **Union with Custom Default Value**  
   Extends union example with a custom default string, showing how defaults work with type hints.
   ```python
   def func(name: str | None = "Bruce Wyane"):
       if name is not None:
           print(f"Hello, {name}")
       else:
         print("hello world")
   
   func()
   ```

7. **Using `typing.Optional` with Import**  
   Demonstrates the older `typing.Optional` syntax as an alternative to `| None`.
   ```python
   import typing
   
   def func(name: typing.Optional[str] = None):
     if name is not None:
           print(f"Hello, {name}")
     else:
         print("hello world")
   
   func()
   ```

8. **List Type Hints with Built-in `list`**  
   Shows type hinting for a list of strings using built-in syntax, with iteration and capitalization.
   ```python
   def func(items: list[str]):
     for item in items:
       print(item.capitalize())
   
   func(['hi', 'hello', 'bye'])
   ```

9. **List Type Hints Using `typing.List`**  
   Uses the older `typing.List` syntax for lists, performing the same operation as above.
   ```python
   from typing import List
   
   def func(items: List[str]):
     for item in items:
       print(item.capitalize())
   
   func(['hi', 'hello', 'bye'])
   ```

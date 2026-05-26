# Day 03
- Path Operation
- Intro to Pydantic model
- async/await
-

## Path Operation
Path Operation is the process of excuting a distinct function when a url path(`/dashboard`) is accessed.
- The Anatomy of a Path Operation
A standard path operation looks like this:

````Python
@app.get("/items")
def read_items():
    return {"message": "Hello World"}
````
This structure is made up of three distinct parts:

The Decorator (``@app.get(...)``)
The decorator associates a specific HTTP method and URL path with your Python function.

``app``: The instance of your FastAPI application (usually created via ``app = FastAPI()``).

``.get``: The Operation (HTTP method). Common operations include:

``.get()`` – To read data.

``.post()`` – To create data.

``.put()`` – To update/replace data.

``.delete()`` – To delete data.

The Path (``"/items"``)
The path is the URL string (relative to your root domain) where this operation lives. For example, if your site is example.com, this endpoint is triggered when a user goes to ``example.com/items``.

The Function (``def read_items():``)
This is the Path Operation Function. It is the standard Python function (or async def function) that executes whenever FastAPI receives a request matching the path and the operation defined above. Whatever this function returns is what FastAPI will send back to the client (usually automatically serialized into ``JSON``).

### Dynamic Paths (Path Parameters)

You can declare path "parameters" or "variables" using the standard Python format string syntax (`{parameter_name}`). FastAPI will automatically extract that value from the URL and pass it into your function as an argument.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

````
- Data Validation: By adding type hints (``item_id: int``), FastAPI automatically validates the incoming request. If a user visits ``/items/foo``, FastAPI will return an  error because ``"foo"``is not an integer.

- Data Conversion: If a user visits ``/items/42``, the function receives the actual Python integer 42, not the string "42".

### Advanced Configuration
You can pass extra arguments into the path operation decorator to document your API or alter its behavior. This information is automatically reflected in your interactive Swagger documentation (``/docs``).

````Python
@app.post(
    "/items/", 
    status_code=201, 
    tags=["Items"], 
    summary="Create a new item"
)
def create_item():
    return {"message": "Item created successfully"}
````
``status_code``: Defines the default HTTP status code returned upon success (e.g., 201 for "Created").

``tags``: Organizes your endpoints into groups in the automatic documentation UI.

``summary``: Provides a quick, human-readable title for the endpoint in the documentation interface.
## Pydantic model

[Pydantic](https://pydantic.dev/) is a Python library to perform data validation.
You declare the "shape" of the data as classes with attributes.

And each attribute has a type.

Then you create an instance of that class with some values and it will validate the values, convert them to the appropriate type (if that's the case) and give you an object with all the data.

And you get all the editor support with that resulting object.

An example from the official Pydantic docs:


````Python 3.10+

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
````

## async/await
no better resource than this [official documentation](https://fastapi.tiangolo.com/async/)
to write ansycronous code with python the syntax is as follows:
````python
# This is a decorator telling FastAPI that whenever a client sends an HTTP GET 
# request to the URL endpoint "/some_path", this specific function should handle it.
@app.get("/some_path")
# 'async def' defines an asynchronous function (a coroutine). This allows FastAPI 
#    to pause this function during idle waiting times (like database queries or API calls) 
#    and handle other incoming requests in the meantime.
async def func():
    #  'await' pauses the execution of func() until some_other_func() finishes its job.
    
    var = await some_other_func()
    
    #  Once the awaited function returns its data and saves it into 'var', 
    #    this line sends that data back to the client as the HTTP response 
    return var
````
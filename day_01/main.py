from fastapi import FastAPI

# create an instance of the FastAPI class
app = FastAPI()

# define a path operation decorator for the root path(GET at "/")
@app.get("/")
async def hello_world():
    # returns a dict, which FastAPI will automatically convert to JSON
    # just like any function, anything can be reurned
    
    return {"message": "Hello, World!"}
# To run the application, use the command: uvicorn main:app --reload
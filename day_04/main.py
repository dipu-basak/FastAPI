from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/dash")
def get_dash():
    return {"title": "Dashboard",
            "message": "welcome to your dashboard"
    }

@app.post("/add_items")
def add_items(item: str):
    # In a real application, you would typically add the item to a database or perform some other action here.
    return {"message": f"Item '{item}' added successfully!"}

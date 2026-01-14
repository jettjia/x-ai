from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="FastAPI CRUD Demo",
    description="A simple CRUD application with FastAPI and SQLAlchemy",
    version="1.0.0"
)

# Include the item routes
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI CRUD Demo!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

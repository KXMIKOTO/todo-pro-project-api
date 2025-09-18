from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Todo Pro Project API is running!"}
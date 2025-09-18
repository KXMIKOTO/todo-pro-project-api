from fastapi import FastAPI

app = FastAPI(title="Smart Todo Pro API")

@app.get("/")
async def root():
    return {"message": "Smart Todo Pro API is running"}
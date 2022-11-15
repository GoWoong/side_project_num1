from fastapi import FastAPI


# fastapi
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

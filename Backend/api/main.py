from fastapi import FastAPI


# fastapi
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

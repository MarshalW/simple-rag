from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import data
import query


app = FastAPI()

data.init()
query.init()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


class QueryRequest(BaseModel):
    query: str = "孔乙己是谁"


@app.post("/query")
async def query_index(request: QueryRequest):
    results = query.query(request.query)
    return StreamingResponse(results.response_gen, media_type="text/event-stream")

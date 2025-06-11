"""
# Simple example of composing API endpoints.

Operation 2 needs to first run Operation 1, then do more stuff. However, we don't
need to duplicate the code of op01 within the definition of the op02 endpoint - we
can just call the op01 endpoint within it.

Same with op03 - it first runs op01, then op02, then does more stuff.
"""
from typing import Dict

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# In-memory cache:
fibonacci_cache: Dict[int, int] = {0: 0, 1: 1}


def fibonacci(n: int) -> int:
    """Calculate the Nth Fibonacci number with caching."""
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Calculate Fibonacci recursively and store in cache
    fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_cache[n]


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/op01")
def operation01(x1: int):
    y1 = fibonacci(x1)  # main operation of this function
    return {"y1": y1}


@app.get("/op02")
def operation02(x1: int):
    response01 = operation01(x1)
    y1 = response01["y1"]

    y2 = y1 + 3  # main operation of this function
    return {"y1": y1, "y2": y2}


@app.get("/op03")
def operation03(x1: int):
    response01 = operation01(x1)
    y1 = response01["y1"]

    response02 = operation02(x1)
    y2 = response02["y2"]

    y3 = y1 / 3  # main operation of this function
    return {"y1": y1, "y2": y2, "y3": y3}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

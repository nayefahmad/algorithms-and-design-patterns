import time

import requests

base_url = "http://127.0.0.1:8001"


def run_op01(x1: int):
    response = requests.get(f"{base_url}/op01?x1={x1}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def run_op02(x1: int):
    response = requests.get(f"{base_url}/op02?x1={x1}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def run_op03(x1: int):
    response = requests.get(f"{base_url}/op03?x1={x1}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    x1 = 50

    start = time.time()
    y1 = run_op01(x1).get("y1")
    interval01 = time.time() - start

    start = time.time()
    y1_1 = run_op01(x1).get("y1")
    interval02 = time.time() - start

    y2 = run_op02(x1).get("y2")
    y3 = run_op03(x1).get("y3")

    print("done")

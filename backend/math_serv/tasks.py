import requests
from . import celery
from .models import Operations
from .config import callback_url

@celery.task(name='compute_the_operation')
def compute_the_operation(op_type, operands):
    res = Operations.calculate(op_type, operands)
    data = {
        "status": "succes",
        "op_type": op_type,
        "operands": operands,
        "result": res
    }
    callback(data)


def on_failure(exc, task_id, args, kwargs, einfo):
    op_type = args[0]
    operands = args[1]
    data = {
        "status": "failure",
        "op_type": op_type,
        "operands": operands,
    }
    callback(data)

def callback(data):
    try:
        r = requests.post(callback_url, json=data)
    except requests.exceptions.RequestException as e:
        print(f"Request failed {e}")




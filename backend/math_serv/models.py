import math
from .helpers import OperationType
from . import db

class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    op_type = db.Column(db.Enum(OperationType), nullable=False)
    operands = db.Column(db.JSON, nullable=False)
    result = db.Column(db.Float, nullable=False)
    
    @classmethod
    def calculate(cls, op_type, operands):
        operation = {
            OperationType.pow_op.name: cls.__calc_pow,
            OperationType.fib_op.name: cls.__calc_fib,
            OperationType.fact_op.name: cls.__calc_fact,
        }.get(op_type)
        res = operation(operands)
        cls(op_type=op_type, operands=operands, result=res).save()
        return res
    
    @staticmethod
    def __calc_pow(operands):
        return math.pow(operands[0], operands[1])
    
    @staticmethod
    def __calc_fib(operands):
        op = operands[0]
        return Operations.__fib(op)

    @staticmethod
    def __fib(op):
        if op == 0:
            return 0
        elif op == 1 or op == 2:
            return 1
        else:
            return Operations.__fib(op-1) + Operations.__fib(op-2)

    @staticmethod
    def __calc_fact(operands):
        return math.factorial(operands[0])
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self



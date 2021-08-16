import enum
from os import name

class OperationType(enum.Enum):
    pow_op = 0
    fib_op = 1
    fact_op = 2

def integral_positive_values(n):
    if n < 0:
        return False
    try:
        return float(n).is_integer()
    except ValueError:
        return False

OpValidation = {
    OperationType.pow_op.name: lambda operands: len(operands) == 2,
    OperationType.fib_op.name: lambda operands: len(operands) == 1 and integral_positive_values(operands[0]),
    OperationType.fact_op.name: lambda operands: len(operands) == 1 and integral_positive_values(operands[0]),
}

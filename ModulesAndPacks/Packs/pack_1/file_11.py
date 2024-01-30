print('This is file', __name__)

# file_11 is in the same directory sd file_12, thus one point needed
from .file_12 import num

def some_func(n: int) -> float:
    return (n + n) / n**n

result = some_func(num)

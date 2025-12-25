from functools import wraps
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} выполнена за {time.time() - start:.4f} сек")
        return result
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}({args})")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

def no_zero_division(func):
    @wraps(func)
    def wrapper(x):
        if x == 0:
            raise ValueError("Деление на ноль запрещено")
        return func(x)
    return wrapper
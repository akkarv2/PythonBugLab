import time
def retry(func, times=3, delay=1):
    for i in range(times):
        try:
            return func()
        except Exception:
            time.sleep(delay)
    raise Exception("failed")
def greet():
    return "hello"
print(retry(greet,3,1))

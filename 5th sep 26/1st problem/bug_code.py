def retry(func, times=3, delay=1):
    for i in range(times):
        try:
            func()
        except Exception:
            time.sleep(delay)
    raise Exception("failed")
def retry_operation(operation, retries=3):
    attempts = 0

    while attempts <= retries:
        try:
            return operation()

        except Exception as error:
            attempts += 1
            print(f"Attempt {attempts} failed: {error}")

    raise Exception("Operation failed after retries")


def read_sensor():
    value = "25.6"

    if value > 20:
        return value

    raise ValueError("Invalid sensor reading")


result = retry_operation(read_sensor)

print(f"Sensor Value: {result}")
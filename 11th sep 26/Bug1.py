def group_readings(readings):
    result = {}

    for device, values in readings.items():
        result[device] = {
            "min": min(values),
            "max": max(values),
            "average": round(sum(values) / len(values), 2)
        }

        if result[device]["average"] > 50:
            result[device]["status"] = "HIGH"
        else:
            result[device]["status"] = "NORMAL"

    return result


readings = {
    "Sensor_A": [40, 55, 60, 45],
    "Sensor_B": [20, 30, 25, 35],
    "Sensor_C": [70, 80, 65, 75]
}

output = group_readings(readings)

for device, data in output.items():
    print(device, "->", data)
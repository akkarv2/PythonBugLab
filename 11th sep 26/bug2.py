def build_processors(config):
    processors = []

    for name, multiplier, offset in config:
        def process(value):
            result = value * multiplier + offset

            if result > 100:
                return f"{name}: HIGH ({result})"
            else:
                return f"{name}: NORMAL ({result})"

        processors.append(process)

    return processors


config = [
    ("TEMP", 2, 10),
    ("PRESSURE", 5, 20),
    ("VOLTAGE", 3, 5),
]

processors = build_processors(config)

values = [20, 15, 30]

output = [processor(value) for processor, value in zip(processors, values)]

for item in output:
    print(item)
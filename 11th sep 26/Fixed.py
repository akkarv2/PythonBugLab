def build_processors(factors):
    processors = []

    for factor in factors:
        def process(value, factor=factor):
            return value * factor

        processors.append(process)

    return processors


factors = [2, 3, 5]
processors = build_processors(factors)

output = [processor(10) for processor in processors]

print(output)
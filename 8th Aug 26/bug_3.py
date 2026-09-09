def calculate_pass_rate(test_results):
    total_tests = len(test_results)
    passed_tests = 0

    for result in test_results:
        if result == "PASS":
            passed_tests += 1

    pass_rate = passed_tests / total_test * 100

    return pass_rate


def generate_report():
    results = [
        "PASS",
        "FAIL",
        "PASS",
        "PASS",
        "FAIL",
        "PASS"
    ]

    rate = calculate_pass_rate

    print(f"Pass Rate: {rate:.2f}%")

    if rate > 80:
        print("Validation successful")
    else:
        print("Validation failed")


generate_report()
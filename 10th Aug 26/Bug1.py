def process_transactions(transactions):
    balances = {}
    successful = 0

    for transaction in transactions:
        user = transaction["user"]
        amount = transaction["amount"]
        transaction_type = transaction["type"]

        if user not in balances:
            balances[user] = 0

        if transaction_type == "deposit":
            balances[user] += amount
            successful += 1

        elif transaction_type == "withdraw":
            if balances[user] >= amount:
                balances[user] -= amount
                successful += 1

        elif transaction_type == "refund":
            balances[user] -= amount
            successful += 1

    return balances, successful


transactions = [
    {"user": "A", "type": "deposit", "amount": 1000},
    {"user": "A", "type": "withdraw", "amount": 300},
    {"user": "A", "type": "withdraw", "amount": 800},
    {"user": "B", "type": "deposit", "amount": 500},
    {"user": "B", "type": "refund", "amount": 100},
    {"user": "C", "type": "withdraw", "amount": 50},
]

balances, successful = process_transactions(transactions)

print("Balances:", balances)
print("Successful transactions:", successful)
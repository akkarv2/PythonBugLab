import json


def load_users(filename):
    file = open(filename,"r")
    data = json.load(file)
    return data


def find_user(users, username):
    for user in users:
        if user["name"].lower() == username:
            return user
    return None


def calculate_average_score(user):
    total = 0

    for score in user["scores"]:
        total += score

    average = total / len(user["score"])
    return average


def main():
    users = load_users(r"F:\PythonBugLab\12th sep 26\users.json")

    username = input("Enter username: ")

    user = find_user(users, username)

    print("User found:", user["name"])

    average = calculate_average_score(user)

    print("Average score:", round(average, 2))


main()
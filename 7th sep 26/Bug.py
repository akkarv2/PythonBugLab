import time
import logging


logging.basicConfig(level=logging.INFO)


def fetch_user_data(user_id, cache={}):
    """
    Fetch user data from a remote service.
    Retries on failure and stores results in cache.
    """

    if user_id in cache:
        return cache[user_id]

    retries = 3

    for attempt in range(retries):
        try:
            user = get_user(user_id)

            if not user:
                raise ValueError("User not found")

            cache[user_id] = user
            return user

        except Exception as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(1)

    return user


def get_user(user_id):
    """
    Simulates API response.
    """

    users = {
        1: {"name": "John", "role": "Admin"},
        2: {"name": "Alice", "role": "User"},
    }

    return users[user_id]


def get_admin_users(user_ids):
    admins = []

    for user_id in user_ids:
        user = fetch_user_data(user_id)

        if user["role"] == "Admin":
            admins.append(user)

    return admins


print(get_admin_users([1, 2, 3]))
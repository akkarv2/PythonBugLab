import time
import logging

logging.basicConfig(level=logging.INFO)


def fetch_user_data(user_id, cache=None):
    """
    Fetch user data from a remote service.
    Retries on failure and stores results in cache.
    """

    if cache is None:
        cache = {}

    if user_id in cache:
        return cache[user_id]

    retries = 3
    last_exception = None

    for attempt in range(retries):
        try:
            user = get_user(user_id)

            if not user:
                raise ValueError("User not found")

            cache[user_id] = user
            return user

        except Exception as e:
            last_exception = e
            logging.error(
                f"Attempt {attempt + 1}/{retries} failed for user {user_id}: {e}"
            )
            time.sleep(1)

    raise last_exception


def get_user(user_id):
    """
    Simulates API response.
    """

    users = {
        1: {"name": "John", "role": "Admin"},
        2: {"name": "Alice", "role": "User"},
    }

    if user_id not in users:
        raise ValueError(f"User {user_id} not found")

    return users[user_id]


def get_admin_users(user_ids):
    admins = []

    for user_id in user_ids:
        try:
            user = fetch_user_data(user_id)

            if user["role"] == "Admin":
                admins.append(user)

        except Exception as e:
            logging.warning(f"Skipping user {user_id}: {e}")

    return admins


print(get_admin_users([1, 2, 3]))
from datetime import time
from typing import List


def validate_time(user_time: List[int], random_time_values: time) -> str:
    """Checks if user_time values are valid."""

    try:
        user_hour, user_minute, user_second = map(int, user_time.split(":"))
    except ValueError:
        return "Invalid format (HH:MM:SS)"

    if not (0 <= user_hour < 24 and 0 <= user_minute < 60 and 0 <= user_second < 60):
        return "Invalid time values"
    elif (
        user_hour % 12 == random_time_values.hour % 12
        and user_minute == random_time_values.minute
        and user_second == random_time_values.second
    ):
        return "Awesomeness, keep up the good work!"
    else:
        return "Oops, try again!"

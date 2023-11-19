from waffle_oak_clock import input_field, validation_label, state
from typing import List

def handle_validation():
    user_time = input_field.get() % 12
    message = validate_time(user_time, state["current_time"])
    validation_label.config(text=message)


def validate_time(user_time: List[int], state):
    current_hour, current_minute, current_second = state.values()

    try:
        user_hour, user_minute, user_second = map(int, user_time.split(":"))
    except ValueError:
        raise ValueError("Invalid format (HH:MM:SS)")

    if not (0 <= user_hour < 12 and 0 <= user_minute < 60 and 0 <= user_second < 60):
        return "Invalid time values"
    elif (
        user_hour == current_hour
        and user_minute == current_minute
        and user_second == current_second
    ):
        return "Awesomeness, keep up the good work!"
    else:
        return "Oops, try again!"

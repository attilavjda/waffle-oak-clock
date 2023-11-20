from datetime import datetime, time
from random import randint


def random_time() -> datetime:
    """Create random hours, minutes and seconds."""
    return time(randint(0, 23), randint(0, 59), randint(0, 59))

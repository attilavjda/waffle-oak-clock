from turtle import RawTurtle

from typing import  NamedTuple
from dataclasses import dataclass

class ClockHands:
    @classmethod
    def get_hour_hand(cls):
        return cls('arrow', 'blue', (1, 10))

    @classmethod
    def get_minute_hand(cls):
        return cls('arrow', 'red', (1, 15))

    @classmethod
    def get_second_hand(cls):
        return cls('arrow', 'gold', (1, 20))

    def __init__(self, shape, color, size):
        self.shape = shape
        self.color = color
        self.size = size


@dataclass
class ClockTime:
    hours: int
    minutes: int
    seconds: int

    @property
    def hours_angle(self) -> float:
        ''' Calculate angle of the hours hand. '''
        return (self.hours % 12) * 360 / 12 + self.minutes * 360 / (12 * 60)

    @property
    def minutes_angle(self) -> float:
        ''' Calculate angle of the minutes hand. '''
        return self.minutes * 360 / 60

    @property
    def seconds_angle(self) -> float:
        ''' Calculate angle of the seconds hand. '''
        return self.seconds * 360 / 60

    @classmethod
    def calculate_angles(cls, random_clock_values: 'ClockTime') -> NamedTuple:
        ''' Calculates hands angles and returns a named tuple. '''
        Angles = NamedTuple('Angles', [('hours', float), ('minutes', float), ('seconds', float)])
        return Angles(
            hours=random_clock_values.hours_angle,
            minutes=random_clock_values.minutes_angle,
            seconds=random_clock_values.seconds_angle
        )

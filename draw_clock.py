from math import radians, sin, cos
from random import randint
from turtle import RawTurtle
from waffle_oak_clock import screen, state, input_field, validation_label, markings_number, markings_radius, markings_hours_size, markings_hours_color, markings_minutes_size, markings_minutes_color
from typing import List, Dict
from tkinter import END
from dataclasses import dataclass

@dataclass
class ClockTime:
    hours: int
    minutes: int
    seconds: int

    @property
    def hours_angle(self) -> float:
        ''' Calculate angle of the hours hand '''
        return (self.hours % 12) * 360 / 12 + self.minutes * 360 / (12 * 60)

    @property
    def minutes_angle(self) -> float:
        ''' Calculate angle of the minutes hand '''
        return self.minutes * 360 / 60

    @property
    def seconds_angle(self) -> float:
        ''' Calculate angle of the seconds hand '''
        return self.seconds * 360 / 60

    @classmethod
    def load_current_time(cls, state: dict) -> 'ClockTime':
        ''' Create a ClockTime instance from the current time in state '''
        current_time = state["current_time"]
        return cls(**current_time)

def calculate_angles(current_time: ClockTime) -> List[float]:
    ''' Calculates hands angles '''
    return [
        current_time.hours_angle,
        current_time.minutes_angle,
        current_time.seconds_angle,
    ]


def draw_hands() -> None:
    ''' Function for drawing the hands, the hands are the actual turtles '''
    current_time = load_current_time()
    hands_angles = calculate_angles(current_time)
    for hand, angle in zip(reversed(clock_hands), reversed(hands_angles)):
        # Set the hands' angles
        hand.setheading(90 - angle)


def random_time_values() -> List[int]:
    ''' Generates random [hours, minutes, seconds] '''
    return [randint(*time) for time in [(0, 11), (0, 59), (0, 59)]]


def refresh_time(state: Dict[str, int]) -> Dict[str, int]:
    ''' Refreshes time in the state dictionary '''
    return dict(zip(state.keys()), random_time_values())


def load_next_clock() -> None:
    ''' 
        Clear the input field and validation message 
        Refresh state with new time values
        Change direction of the hand  turtles
    '''
    input_field.delete(0, END)
    validation_label.config(text="")
    state["current_time"] = refresh_time(state["current_time"])
    draw_hands()


# Create a turtle to draw the clock face
clock = RawTurtle(screen)
clock.speed(100)



# Make turtles for clock hands
clock_hands = []
for hand_name, hand_config in config["hands"].items():
    hand = RawTurtle(screen)
    hand.shape(hand_config["shape"])
    hand.color(hand_config["color"])
    hand.shapesize(
        stretch_wid=hand_config["size"][0], stretch_len=hand_config["size"][1]
    )
    clock_hands.append(hand)

[]



def draw_markings() -> None:
    for i in range(markings_number):
        angle = radians(i * 360 / markings_number)
        x = markings_radius * sin(angle)
        y = -markings_radius * cos(angle)

        if i % 5 == 0:
            # Larger dot for hours
            clock.penup()
            clock.goto(x, y)
            clock.dot(markings_hours_size, markings_hours_color)
        elif i % 1 == 0:
            # Smaller dot for minutes
            clock.penup()
            clock.goto(x, y)
            clock.dot(markings_minutes_size, markings_minutes_color)

# Draw hands
draw_hands()

from datetime import time
from math import cos, radians, sin
from tkinter import END, Button, Canvas, Entry, Frame, Label, Tk
from turtle import RawTurtle, TurtleScreen
from typing import List

from draw_clock import ClockHands, ClockTime
from random_time import random_time
from validation import validate_time


def main(
    screen_title: str = "Clock Validation",
    screen_canvas_width: int = 600,
    screen_canvas_height: int = 600,
    nav_title: str = "Navigation Window",
    nav_label_text: str = "Validate time value (HH:MM:SS)",
    theme_bg: List = ["black", "white"],
    light_mode_on: bool = True,
    random_time_values: time = random_time(),
    markings_radius: int = 220,
    markings_number: int = 60,
    markings_hours_color: str = "blue",
    markings_hours_size: int = 10,
    markings_minutes_color: str = "green",
    markings_minutes_size: int = 5,
    buttons_validate_text: str = "Validate Time",
    buttons_next_text: str = "Next Clock",
    buttons_theme_text: List = ["☀️", "🌘"],
):
    def handle_validation() -> None:
        """ Updates validation_label text with result of validation. """
        user_time: str = input_field.get()
        print(user_time)
        message: str = validate_time(user_time, random_time_values)
        validation_label.config(text=message)

    def load_next_clock() -> None:
        """
        Clears the input field and validation message.
        Updates random_time variable with new time values.
        Changes direction of the hand turtles.
        """
        nonlocal random_time_values
        input_field.delete(0, END)
        validation_label.config(text=nav_label_text)
        random_time_values = random_time()
        draw_hands(random_time_values)

    def theme_toggle() -> None:
        """
        Switches background color with `screen.bgcolor(color)` and switches theme_button text.
        """
        nonlocal light_mode_on
        screen.bgcolor(theme_bg[light_mode_on])
        theme_button.config(text=buttons_theme_text[light_mode_on])
        light_mode_on = not light_mode_on

    def create_turtle(hand: ClockHands) -> RawTurtle:
        ''' Creates a turtle with shape, color and size given in ClockHands of draw_clock.py. '''
        hand_turtle = RawTurtle(screen)
        hand_turtle.shape(hand.shape)
        hand_turtle.color(hand.color)
        hand_turtle.shapesize(*hand.size)
        hand_turtle.speed(1)
        return hand_turtle

    # Create tkinter GUI for interaction
    root = Tk()
    root.title(screen_title)

    # Create a Canvas to hold the Turtle screen
    canvas = Canvas(
        root,
        width=screen_canvas_width,
        height=screen_canvas_height,
    )
    canvas.pack()

    # Create a Turtle screen within the canvas
    screen = TurtleScreen(canvas)
    screen.bgcolor(theme_bg[not light_mode_on])

    # Create a Frame to hold the button
    button_frame = Frame(root)
    button_frame.pack(side="bottom", fill="both", expand=True)

    # Create the input field and buttons
    input_field = Entry(button_frame)
    input_field.pack()

    # Create validation label
    validation_label = Label(button_frame, text=nav_label_text)
    validation_label.pack()

    # Create validate button
    validate_button = Button(
        button_frame, text=buttons_validate_text, command=handle_validation
    )
    validate_button.pack()

    # Create next button
    next_clock_button = Button(
        button_frame, text=buttons_next_text, command=load_next_clock
    )
    next_clock_button.pack()

    # Create theme toggle
    theme_button = Button(
        button_frame, text=buttons_theme_text[not light_mode_on], command=theme_toggle
    )
    theme_button.pack()

    # Create a turtle to draw the clock face
    clock = RawTurtle(screen)
    clock.speed(100)

    hour_hand = ClockHands.get_hour_hand()
    minute_hand = ClockHands.get_minute_hand()
    second_hand = ClockHands.get_second_hand()

    clock_hands = [hour_hand, minute_hand, second_hand]

    hour_turtle, minute_turtle, second_turtle = [
        create_turtle(hand) for hand in clock_hands
    ]

    clock_turtles = [hour_turtle, minute_turtle, second_turtle]

    def draw_markings() -> None:
        """Draws the markings of the clock. """
        for minute in range(markings_number):
            angle = radians(minute * 360 / markings_number)
            x = markings_radius * sin(angle)
            y = -markings_radius * cos(angle)

            clock.penup()
            clock.goto(x, y)
            if minute % 5 == 0:
                clock.dot(markings_hours_size, markings_hours_color)
            else:
                clock.dot(markings_minutes_size, markings_minutes_color)

    def draw_hands(random_time_values: time) -> None:
        """
        Function for setting hands direction, the hands are actual turtles.
        Updates hand turtle values.
        """
        clock_time_instance = ClockTime(
            random_time_values.hour,
            random_time_values.minute,
            random_time_values.second,
        )
        angles_namedtuple = ClockTime.calculate_angles(clock_time_instance)
        for hand, angle in zip(
            reversed(clock_turtles), reversed(angles_namedtuple._asdict().values())
        ):
            hand.setheading(90 - angle)

    draw_markings()

    draw_hands(random_time_values)

    # Start the tkinter main loop to manage the GUI
    root.mainloop()


if __name__ == "__main__":
    main()

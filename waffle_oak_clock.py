from datetime import datetime
from tkinter import Tk, Canvas, Frame, Entry, Button, Label
from turtle import TurtleScreen, RawTurtle

from validation import handle_validation, load_next_clock
from gui_logic import toggle_theme


def main(
    screen_title: str="Clock Validation",
    screen_canvas_width: int=600,
    screen_canvas_height: int=600,
    nav_title: str="Navigation Window",
    nav_label_text: str="Validate time value (HH:MM:SS)",
    theme_light_bg: str="white",
    theme_dark_bg: str="black",

    markings_radius: int=220,
    markings_number: int=60,
    markings_hours_color: str="blue",
    markings_hours_size: int= 10,
    markings_minutes_color: str="green",
    markings_minutes_size: int=5,

    buttons_validate_text: str="Validate Time",    
    buttons_next_text: str="Next Clock",
    buttons_theme_dark_text: str="🌘",
    buttons_theme_light_text: str="☀️",
):

    state = {
        "theme": {
            'theme_bg': ['dark_bg', 'light_bg']
        },
        "current_time": {
            "hours": datetime.now().hour,
            "minute": datetime.now().minute,
            "seconds": datetime.now().second,
        },
    }

    # Create tkinter GUI for interaction
    root = Tk()
    root.title(screen_title)

    # Start the tkinter main loop to manage the GUI
    root.mainloop()


    # Create a Canvas to hold the Turtle screen 
    canvas = Canvas(
        root,
        width=screen_canvas_width,
        height=screen_canvas_height,
    )
    canvas.pack()

    # Create a Frame to hold the button
    button_frame = Frame(root)
    button_frame.pack(side="bottom", fill="both", expand=True)

    # Create the input field and buttons
    input_field = Entry(button_frame)
    input_field.pack()

    # Create validate button
    validate_button = Button(
        button_frame, text=buttons_validate_text, command=handle_validation
    )
    validate_button.pack()

    # Create validation label
    validation_label = Label(button_frame, text=nav_label_text)
    validation_label.pack()

    # Create next button
    next_clock_button = Button(
        button_frame, text=buttons_next_text, command=load_next_clock
    )
    next_clock_button.pack()

    # Create theme toggle:
    theme_button = Button(
        button_frame, text=buttons_theme_light_text, command=toggle_theme
    )
    theme_button.pack()


    # Create a Turtle screen within the canvas
    screen = TurtleScreen(canvas)
    screen.bgcolor(state["theme"]["theme_bg"])

    # Create a turtle to draw the clock face
    clock = RawTurtle(screen)
    clock.speed(100)

if __name__ == "__main__":
    main()

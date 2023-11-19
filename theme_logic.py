from waffle_oak_clock import state

def toggle_theme():
    ''' If it is light mode, switch to dark and vice versa '''
    state["theme"]["theme_bg"] = not state["theme"]["theme_bg"]

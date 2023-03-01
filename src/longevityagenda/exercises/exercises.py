import toga

def build(window):
    # Create the main box
    main_box = toga.Box()

    # Create the exercises label
    exercises_label = toga.Label('Exercises', style=Pack(padding=10))

    # Add the exercises label to the main box
    main_box.add(exercises_label)

    return main_box

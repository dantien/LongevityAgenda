import toga
from toga.style.pack import *

class ProgressView(toga.Box):
    def __init__(self):
        super().__init__()

        self.heading = toga.Label(
            'Progress',
            style=Pack(text_align=CENTER, font_weight=BOLD, font_size=24)
        )

        # Create a progress bar with an initial value of 0
        self.progress_bar = toga.ProgressBar(max=100, value=0)

        # Create a button to simulate progress
        self.progress_button = toga.Button(
            'Make Progress',
            on_press=self.update_progress
        )

        # Add the progress bar and button to the box
        self.add(self.heading, self.progress_bar, self.progress_button)

    def update_progress(self, widget):
        # Update the progress bar value
        self.progress_bar.value += 10

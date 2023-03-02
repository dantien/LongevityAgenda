import toga
from toga.style.pack import *

class HealthView:
    def __init__(self):
        self.box = toga.Box()

        # Create the heading label
        heading_label = toga.Label(
            'Health',
            style=Pack(text_align=CENTER, font_weight=BOLD, font_size=24, padding_top=20)
        )

        # Create the health features box
        health_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 10)))
        health_label = toga.Label(
            'Today\'s Health Metrics',
            style=Pack(font_weight=BOLD, font_size=18)
        )
        health_table = toga.Table(
            headings=['Metric', 'Value'],
            data=[
                ['Blood Pressure', '120/80'],
                ['Heart Rate', '70 bpm'],
                ['Temperature', '98.6 F'],
                ['Blood Sugar', '90 mg/dL']
            ],
            style=Pack(flex=1, padding_top=10)
        )
        refresh_button = toga.Button(
            'Refresh',
            on_press=self.refresh_health_metrics,
            style=Pack(padding=(0, 10))
        )
        health_box.add(health_label)
        health_box.add(health_table)
        health_box.add(refresh_button)

        # Add all boxes to main box
        self.box.add(heading_label)
        self.box.add(health_box)

    def refresh_health_metrics(self, widget):
        # Code to refresh the displayed health metrics
        pass

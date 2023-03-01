import toga
from datetime import datetime
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CalendarView(toga.Box):
    def __init__(self, heading='Calendar', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Create the calendar widget
        self.calendar = toga.Calendar(on_select_date=self.on_select_date)

        # Add the calendar widget to the box
        self.add(
            self.heading_label,
            self.calendar,
            style=Pack(direction=COLUMN, padding=10)
        )

    def on_select_date(self, widget, date):
        # Handle the selection of a date
        print(f"Selected date: {date.strftime('%m/%d/%Y')}")


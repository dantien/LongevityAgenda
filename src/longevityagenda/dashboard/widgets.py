import toga
from toga.style import Pack

class DashboardItem:
    def __init__(self, title, description, icon):
        self.title = title
        self.description = description
        self.icon = icon
        
        self.button = toga.Button(
            label=title,
            on_press=self.on_press,
            style=Pack(flex=1)
        )
        
    def on_press(self, widget):
        # Code to handle button press
        pass

class AddItemDialog:
    def __init__(self):
        self.box = toga.Box()
        self.text_input = toga.TextInput()
        self.button = toga.Button(
            label='Add Item',
            on_press=self.add_item
        )
        self.box.add(self.text_input)
        self.box.add(self.button)
        
    def add_item(self, widget):
        title = self.text_input.value
        # Code to add item to dashboard
        
class ConfirmationDialog:
    def __init__(self, message, on_confirm, on_cancel):
        self.box = toga.Box()
        self.message_label = toga.Label(
            text=message,
            style=Pack(padding_bottom=10)
        )
        self.confirm_button = toga.Button(
            label='Confirm',
            on_press=on_confirm,
            style=Pack(padding_right=10)
        )
        self.cancel_button = toga.Button(
            label='Cancel',
            on_press=on_cancel
        )
        self.box.add(self.message_label)
        self.box.add(self.confirm_button)
        self.box.add(self.cancel_button)

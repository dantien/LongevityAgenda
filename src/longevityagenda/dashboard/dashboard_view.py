from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from .widgets import DashboardItem, AddItemDialog, ConfirmationDialog


class DashboardView:
    def __init__(self):
        self.items = []

        # Create the main box containing the header and items
        self.box = Box(style=Pack(direction=COLUMN, padding_top=10))

        # Create the header
        header_box = Box(style=Pack(direction=ROW, padding=(0, 5)))
        header_label = Label('Dashboard', style=Pack(flex=1, font_size=18))
        add_button = Button('Add', on_press=self.show_add_item_dialog)
        header_box.add(header_label)
        header_box.add(add_button)
        self.box.add(header_box)

        # Create the box containing the dashboard items
        self.items_box = Box(style=Pack(direction=COLUMN, padding=(10, 0)))
        self.box.add(self.items_box)

    def add_item(self, item):
        # Add the item to the list of items
        self.items.append(item)

        # Add the item to the dashboard
        item_box = Box(style=Pack(direction=ROW, padding=(0, 5)))
        item_box.add(item.label)
        item_box.add(item.value_label)
        delete_button = Button('Delete', on_press=lambda widget: self.show_confirmation_dialog(item))
        item_box.add(delete_button)
        self.items_box.add(item_box)

    def show_add_item_dialog(self, widget):
        # Create the dialog
        dialog = AddItemDialog(on_add=lambda label, value: self.add_item(DashboardItem(label, value)))

        # Show the dialog
        dialog.show()

    def show_confirmation_dialog(self, item):
        # Create the dialog
        dialog = ConfirmationDialog(
            'Delete item?',
            f'Are you sure you want to delete the item "{item.label.text}"?',
            on_confirm=lambda widget: self.delete_item(item)
        )

        # Show the dialog
        dialog.show()

    def delete_item(self, item):
        # Remove the item from the list of items
        self.items.remove(item)

        # Remove the item from the dashboard
        self.items_box.remove(item.box)

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class SocialView(toga.Box):
    def __init__(self, heading='Social Feed', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Create a list to display social feed
        self.social_list = toga.List(style=Pack(flex=1))

        # Create a box to contain the post entry widgets
        self.post_box = toga.Box(style=Pack(direction=ROW, padding=5))

        # Create input widgets for post content and author
        self.post_content_input = toga.TextInput(
            placeholder='What\'s on your mind?',
            style=Pack(flex=1, padding=(0, 5))
        )
        self.post_author_input = toga.TextInput(
            placeholder='Author',
            style=Pack(width=120, padding=(0, 5))
        )

        # Create a button to submit the new post
        self.post_button = toga.Button(
            'Post',
            on_press=self.add_post,
            style=Pack(width=80)
        )

        # Add the post input widgets and button to the post box
        self.post_box.add(self.post_content_input)
        self.post_box.add(self.post_author_input)
        self.post_box.add(self.post_button)

        # Add all widgets to the main box
        self.add(
            self.heading_label,
            self.social_list,
            self.post_box,
            style=Pack(direction=COLUMN)
        )

    def add_post(self, widget):
        # Get the new post content and author from the input widgets
        content = self.post_content_input.value
        author = self.post_author_input.value

        # Create a new post entry string and add it to the social feed list
        post_entry = f'{author}: {content}'
        self.social_list.data.append(post_entry)
        self.post_content_input.clear()
        self.post_author_input.clear()

import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class SocialFeatures:
    def __init__(self):
        self.results_sharing = toga.Button('Results Sharing', on_press=self.results_sharing_handler)
        self.follow_users = toga.Button('Following Other Users', on_press=self.follow_users_handler)
        self.community_access = toga.Button('Access to Community', on_press=self.community_access_handler)
        self.box = toga.Box(style=Pack(direction=COLUMN))
        self.box.add(self.results_sharing)
        self.box.add(self.follow_users)
        self.box.add(self.community_access)

    def results_sharing_handler(self, widget):
        # Code to handle results sharing feature
        pass

    def follow_users_handler(self, widget):
        # Code to handle following other users feature
        pass

    def community_access_handler(self, widget):
        # Code to handle access to community feature
        pass

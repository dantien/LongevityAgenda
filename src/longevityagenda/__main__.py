import csv
import os

import toga
from toga.style.pack import COLUMN, Pack

from longevityagenda.views.about_view import AboutView
from longevityagenda.views.calendar_view import CalendarView
from longevityagenda.views.challenges_view import ChallengesView
from longevityagenda.dashboard.dashboard_view import DashboardView
from longevityagenda.views.fitness_view import FitnessView
from longevityagenda.views.health_view import HealthView
from longevityagenda.views.login_view import LoginView
from longevityagenda.views.main_view import MainView
from longevityagenda.views.profile_view import ProfileView
from longevityagenda.views.progress_view import ProgressView
from longevityagenda.views.settings_view import SettingsView


# Constants
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CHALLENGES_FILE = os.path.join(DATA_DIR, 'challenges.csv')


def load_challenges():
    challenges = []
    with open(CHALLENGES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            challenges.append(row)
    return challenges


class LongevityAgenda(toga.App):
    def __init__(self, name, organization):
        super().__init__(name, organization)

        # Load challenges
        self.challenges = load_challenges()

        # Set up main window and view
        self.main_view = MainView(app=self)

    def startup(self):
        # Set up main window
        self.main_window = self.main_view.main_window
        self.main_window.app = self

        # Set up menu
        file_menu = toga.Menu('File')
        help_menu = toga.Menu('Help')
        about_item = toga.MenuItem('About Longevity Agenda', action=self.show_about)
        file_menu.add(about_item)

        # Set up toolbar
        self.toolbar = toga.Toolbar()
        dashboard_button = toga.Button('Dashboard', on_press=self.show_dashboard, style=Pack(padding=5))
        challenges_button = toga.Button('Challenges', on_press=self.show_challenges, style=Pack(padding=5))
        progress_button = toga.Button('Progress', on_press=self.show_progress, style=Pack(padding=5))
        calendar_button = toga.Button('Calendar', on_press=self.show_calendar, style=Pack(padding=5))
        self.toolbar.add(dashboard_button, challenges_button, progress_button, calendar_button)

        # Add menu and toolbar to main window
        self.main_window.toolbar = self.toolbar
        self.main_window.menu = toga.MenuBar(file_menu=file_menu, help_menu=help_menu)

        # Show main window
        self.main_window.show()

    def show_about(self, widget):
        about_window = AboutView()
        about_window.app = self
        about_window.show()

    def show_dashboard(self, widget):
        dashboard_window = DashboardView(app=self)
        self.main_view.main_window.content = dashboard_window

    def show_challenges(self, widget):
        challenges_window = ChallengesView(self.challenges, app=self)
        self.main_view.main_window.content = challenges_window

    def show_calendar(self, widget):
        calendar_window = CalendarView()
        calendar_window.app = self
        self.main_view.main_window.content = calendar_window

    def show_progress(self, widget):
        progress_window = ProgressView(app=self)
        self.main_view.main_window.content = progress_window

    def show_health(self, widget):
        health_window = HealthView()
        health_window.app = self
        self.main_view.main_window.content = health_window

    def show_fitness(self, widget):
        fitness_window = FitnessView()
        fitness_window.app = self
        self.main_view.main_window.content = fitness_window

    def show_login(self, widget):
        login_window = LoginView(app=self)
        login_window.app = self
        self.main_window.content = login_window

    def show_profile(self, widget):
        profile_window = ProfileView(app=self)
        self.main_view.main_window.content = profile_window

    def save_settings(self, widget):
        self.settings_view.save_settings()

    def show_settings(self, widget):
        settings_window = self.settings_view.settings_window
        settings_window.app = self
        settings_window.show()

    def main():
        return LongevityAgenda('Longevity Agenda', 'org.pybee')
    
    if __name__ == '__main__':
        main().main_loop()

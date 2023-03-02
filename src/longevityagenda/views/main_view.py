# views/main_view.py

from toga import App, MainWindow
from longevityagenda.views.about_view import AboutView
from longevityagenda.views.calendar_view import CalendarView
from longevityagenda.views.challenges_view import ChallengesView
from longevityagenda.dashboard.dashboard_view import DashboardView
from longevityagenda.views.fitness_view import FitnessView
from longevityagenda.views.health_view import HealthView
from longevityagenda.views.login_view import LoginView
from longevityagenda.views.profile_view import ProfileView
from longevityagenda.views.progress_view import ProgressView
from longevityagenda.views.settings_view import SettingsView
from longevityagenda.views.signup_view import SignupView
from longevityagenda.views.social_view import SocialView
from longevityagenda.views.features import FEATURES

class MainView:
    def __init__(self):
        self.app = App('Longevity Agenda', 'org.longevityagenda')
        self.main_window = MainWindow(title='Longevity Agenda', size=(800, 600))

        # Initialize views
        self.about_view = AboutView()
        self.calendar_view = CalendarView()
        self.challenges = [
            {'title': '30-Day Yoga Challenge'},
            {'title': '10,000 Steps a Day Challenge'},
            {'title': 'Whole30 Challenge'},
            {'title': 'Couch to 5K Challenge'},
            {'title': 'Meditation Challenge'}
        ]
        self.challenges_view = ChallengesView(challenges=self.challenges)
        self.dashboard_view = DashboardView()
        self.fitness_view = FitnessView()
        self.health_view = HealthView()
        self.login_view = LoginView()
        self.profile_view = ProfileView()
        self.progress_view = ProgressView()
        self.settings_view = SettingsView()
        self.signup_view = SignupView()
        self.social_view = SocialView()

        # Set the default view to the login view
        self.main_window.content = self.login_view.box

        # Create menus
        self.create_menus()

    def create_menus(self):
        file_menu = self.app.main_menu.add('File')
        file_menu.add('Save')
        file_menu.add('Exit', on_press=self.exit_app)

        view_menu = self.app.main_menu.add('View')
        view_menu.add('Dashboard', on_press=self.show_dashboard_view)
        view_menu.add('Fitness', on_press=self.show_fitness_view)
        view_menu.add('Health', on_press=self.show_health_view)
        view_menu.add('Social', on_press=self.show_social_view)
        view_menu.add('Calendar', on_press=self.show_calendar_view)
        view_menu.add('Progress', on_press=self.show_progress_view)
        view_menu.add('Challenges', on_press=self.show_challenges_view)

        settings_menu = self.app.main_menu.add('Settings')
        settings_menu.add('Profile', on_press=self.show_profile_view)
        settings_menu.add('Signup', on_press=self.show_signup_view)
        settings_menu.add('About', on_press=self.show_about_view)

    def exit_app(self, widget):
        self.app.exit()

    # Methods to switch views
    def show_about_view(self, widget):
        self.main_window.content = self.about_view.box

    def show_calendar_view(self, widget):
        self.main_window.content = self.calendar_view.box

    def show_challenges_view(self, widget):
        self.main_window.content = self.challenges_view.box

    def show_dashboard_view(self, widget):
        self.main_window.content = self.dashboard_view.box

    def show_fitness_view(self, widget):
        self.main_window.content = self.fitness_view.box

    def show_health_view(self, widget):
        self.main_window.content = self.health_view.box

    def show_login_view(self, widget):
        self.main_window.content = self.login_view

    def show_profile_view(self, widget):
        self.main_window.content = self.profile_view.box

    def show_progress_view(self, widget):
        self.main_window.content = self.progress_view.box

    def show_settings_view(self, widget):
        self.main_window.content = self.settings_view.box

    def show_signup_view(self, widget):
        self.main_window.content = self.signup_view.box

    def show_social_view(self, widget):
        self.main_window.content = self.social_view.box

    def show_health_view(self, widget):
        self.main_window.content = self.health_view.box

    def show_fitness_view(self, widget):
        self.main_window.content = self.fitness_view.box

    def show_dashboard_view(self, widget):
        self.main_window.content = self.dashboard_view.box

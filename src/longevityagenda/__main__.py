from longevityagenda.views.about_view import AboutView
from longevityagenda.views.calendar_view import CalendarView
from longevityagenda.views.challenges_view import ChallengesView
from longevityagenda.views.fitness_view import FitnessView
from longevityagenda.views.login_view import LoginView
from longevityagenda.views.main_view import MainView
from longevityagenda.views.profile.profile_view import ProfileView
from longevityagenda.views.progress_view import ProgressView
from longevityagenda.views.settings_view import SettingsView
from longevityagenda.views.shop_view import ShopView
from longevityagenda.views.signup_view import SignupView

if __name__ == '__main__':
    views = [AboutView, CalendarView, ChallengesView, FitnessView, LoginView,
             MainView, ProfileView, ProgressView, SettingsView, ShopView, SignupView]
    for view in views:
        view().present()

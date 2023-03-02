# features.py

class Feature:
    def __init__(self, name, icon=None, description=None):
        self.name = name
        self.icon = icon
        self.description = description

class Features:
    ALL_FEATURES = [
        Feature('Calendar', icon='icons/calendar.png', description='View and manage your schedule'),
        Feature('Challenges', icon='icons/challenges.png', description='Set and track personal challenges'),
        Feature('Fitness', icon='icons/fitness.png', description='Track your workouts and fitness metrics'),
        Feature('Health', icon='icons/health.png', description='Track your health data and vitals'),
        Feature('Profile', icon='icons/profile.png', description='View and manage your personal information'),
        Feature('Progress', icon='icons/progress.png', description='Track your progress and set goals'),
        Feature('Settings', icon='icons/settings.png', description='Manage app settings and preferences'),
        Feature('Social', icon='icons/social.png', description='Connect and share with others'),
        Feature('Dashboard', icon='icons/dashboard.png', description='View your overall progress and stats')
    ]

    def __init__(self):
        self.features = Features.ALL_FEATURES

    def get_feature_by_name(self, name):
        for feature in self.features:
            if feature.name == name:
                return feature
        return None

    def add_feature(self, name, icon=None, description=None):
        new_feature = Feature(name, icon, description)
        self.features.append(new_feature)

    def remove_feature(self, feature):
        self.features.remove(feature)

    def get_feature_names(self):
        return [feature.name for feature in self.features]

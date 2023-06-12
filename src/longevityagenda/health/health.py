import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class HealthFeatures:
    def __init__(self):
        self.baseline = toga.Button('Establishing a Baseline', on_press=self.baseline_handler)
        self.aerob_fitness = toga.Button('Building Aerobic Fitness', on_press=self.aerob_fitness_handler)
        self.progress_monitor = toga.Button('Monitoring Progress', on_press=self.progress_monitor_handler)
        self.heart_rate_integration = toga.Button('Integration with Heart Rate Monitors',
                                                  on_press=self.heart_rate_integration_handler)
        self.sleep_monitoring = toga.Button('Sleep Monitoring', on_press=self.sleep_monitoring_handler)
        self.box = toga.Box(style=Pack(direction=COLUMN))
        self.box.add(self.baseline)
        self.box.add(self.aerob_fitness)
        self.box.add(self.progress_monitor)
        self.box.add(self.heart_rate_integration)
        self.box.add(self.sleep_monitoring)

    def baseline_handler(self, widget):
        # Code to handle establishing a baseline feature
        pass

    def aerob_fitness_handler(self, widget):
        # Code to handle building aerobic fitness feature
        pass

    def progress_monitor_handler(self, widget):
        # Code to handle monitoring progress feature
        pass

    def heart_rate_integration_handler(self, widget):
        # Code to handle integration with heart rate monitors feature
        pass

    def sleep_monitoring_handler(self, widget):
        # Code to handle sleep monitoring feature
        pass

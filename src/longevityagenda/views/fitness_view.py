import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class FitnessView(toga.Box):
    def __init__(self, heading='Fitness', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Add calorie count button
        self.calorie_count_button = toga.Button(
            'Calorie Count',
            on_press=self.calorie_count_handler,
            style=Pack(flex=1)
        )

        # Add distance and speed measurement button
        self.distance_speed_button = toga.Button(
            'Distance and Speed Measurement',
            on_press=self.distance_speed_handler,
            style=Pack(flex=1)
        )

        # Add training planner button
        self.training_planner_button = toga.Button(
            'Training Planner',
            on_press=self.training_planner_handler,
            style=Pack(flex=1)
        )

        # Add step counter button
        self.step_counter_button = toga.Button(
            'Step Counter',
            on_press=self.step_counter_handler,
            style=Pack(flex=1)
        )

        # Add goals and milestones button
        self.goals_milestones_button = toga.Button(
            'Goals and Milestones',
            on_press=self.goals_milestones_handler,
            style=Pack(flex=1)
        )

        # Add MAF training sessions button
        self.maf_training_button = toga.Button(
            'MAF Training Sessions',
            on_press=self.maf_training_handler,
            style=Pack(flex=1)
        )

        # Add strength training button
        self.strength_training_button = toga.Button(
            'Strength Training',
            on_press=self.strength_training_handler,
            style=Pack(flex=1)
        )

        # Add all buttons to the box
        self.add(
            self.heading_label,
            self.calorie_count_button,
            self.distance_speed_button,
            self.training_planner_button,
            self.step_counter_button,
            self.goals_milestones_button,
            self.maf_training_button,
            self.strength_training_button,
            style=Pack(direction=COLUMN)
        )

    def calorie_count_handler(self, widget):
        # Handle calorie count button press
        print('Calorie count button pressed')

    def distance_speed_handler(self, widget):
        # Handle distance and speed measurement button press
        print('Distance and speed measurement button pressed')

    def training_planner_handler(self, widget):
        # Handle training planner button press
        print('Training planner button pressed')

    def step_counter_handler(self, widget):
        # Handle step counter button press
        print('Step counter button pressed')

    def goals_milestones_handler(self, widget):
        # Handle goals and milestones button press
        print('Goals and milestones button pressed')

    def maf_training_handler(self, widget):
        # Handle MAF training sessions button press
        print('MAF training sessions button pressed')

    def strength_training_handler(self, widget):
        # Handle strength training button press
        print('Strength training button pressed')

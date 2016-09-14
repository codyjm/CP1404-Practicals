"""
Convert miles to kilometres with Kivy GUI
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_m_to_km.kv")
        Window.size = (400, 200)
        return self.root

    def handle_convert(self):
        miles = self.get_valid_input()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.get_valid_input() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_convert()

    def get_valid_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

ConvertToKm().run()

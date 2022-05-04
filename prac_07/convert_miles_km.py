"""
GUI program for converting miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesConverter(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        miles = self.convert_to_float(text)
        self.result(miles)

    def handle_increment(self, text, change):
        miles = self.convert_to_float(text) + change
        self.root.ids.input_miles.text = str(miles)

    def result(self, miles):
        self.output_km = str(miles * 1.60934)

    @staticmethod
    def convert_to_float(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverter().run()

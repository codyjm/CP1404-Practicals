"""
Loop through a list of strings, display each string as a separate label
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DisplayList(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = ["I", "am", "amazing"]

    def build(self):
        self.title = "String List"
        self.root = Builder.load_file("string_list.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for item in self.items:
            temp_button = Button(text=item)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.item_box.add_widget(temp_button)

    def press_entry(self, instance):
        # instance is to get the text from the label?

        self.status_text = "{}".format(instance.text)

DisplayList().run()

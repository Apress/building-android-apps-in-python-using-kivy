import kivy.app
import kivy.lang

class TestApp(kivy.app.App):

    def button1_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input1'].text

    def button2_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input2'].text

    def build(self):
        return kivy.lang.Builder.load_string(
"""
BoxLayout:
    orientation: "vertical"
    Label:
        text: "Waiting for Button Press"
        id: text_label
    BoxLayout:
        orientation: "horizontal"
        TextInput:
            text: "TextInput 1"
            id: text_input1
        Button:
            text: "Click me"
            on_press: app.button1_press()
    BoxLayout:
        orientation: "horizontal"
        TextInput:
            text: "TextInput 2"
            id: text_input2
        Button:
            text: "Click me"
            on_press: app.button2_press()
""")

app = TestApp()
app.run()

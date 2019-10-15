import kivy.app
import kivy.lang

class TestApp(kivy.app.App):

    def button1_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input1'].text

    def button2_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input2'].text

    def build(self):
        return kivy.lang.Builder.load_file("test1.kv")

app = TestApp()
app.run()

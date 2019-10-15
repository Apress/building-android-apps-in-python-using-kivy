import kivy.app

class TestApp(kivy.app.App):

    def button1_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input1'].text

    def button2_press(self):
        self.root.ids['text_label'].text = self.root.ids['text_input2'].text

app = TestApp()
app.run()

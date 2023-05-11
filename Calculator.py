from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        root = BoxLayout()
        output = Label()
        button = ('1', '2', '3',
                  '4','5','6',
                  '7','8','9',
                  '+','-', '*',
                  '/', '=','AC')
        button_layout = GridLayout(cols=4, size_hint_y=0)
        for symbol in button:
            button_layout.add_widget(Button(text=symbol))

        def print_button_text(input):
            output.text += input.text

        for button in button_layout.children[2:]:
            button.bind(on_press=print_button_text)


        def evaluate_result(self):
            output.text = str(eval(output.text))

        def clear(self):
            output.text = ''


        button_layout.children[1].bind(on_press=evaluate_result)
        button_layout.children[0].bind(on_press=clear)

        root.add_widget(output)
        root.add_widget(button_layout)

        return root


MyApp().run()

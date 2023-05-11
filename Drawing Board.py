from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line,Color

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width = 10)

    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


class DrawingApp(App):
    def build(self):
        root = DrawingWidget()
        return root


DrawingApp().run()
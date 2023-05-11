from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class DrawingWidget(Widget):
    def on_touch_down(self,touch):
        super(DrawingWidget,self).on_touch_down(touch)
        with self.canvas:
            self.line = Line(points=[touch.pos[0],touch.pos[1]],width = 0)
    def on_touch_move(selfself,touch):
        self.line.points = self.line.points + [touch.pos[0],touch.pos[1]]


DrawingWidget().run()


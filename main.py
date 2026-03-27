import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class MinimalApp(App):
    def build(self):
        self.label = Label(text="Iniciando...", font_size=40)
        Clock.schedule_once(self.cambiar_texto, 2)
        return self.label
    
    def cambiar_texto(self, dt):
        self.label.text = "✅ FUNCIONA!\nApp correcta"

if __name__ == '__main__':
    MinimalApp().run()
import kivy

from kivy.uix.gridlayout import GridLayout

from kivy.app import App
from kivy.lang import Builder

import LabelB

Builder.load_string("""
<MyGrid>:
  rows: 2
  LabelB:
    bcolor: 1,0,0,1
  LabelB:
    bcolor: 0,1,0,1
""")

class MyGrid(GridLayout):
    pass

class TheApp(App):
    def build(self):
        return MyGrid()

TheApp().run()

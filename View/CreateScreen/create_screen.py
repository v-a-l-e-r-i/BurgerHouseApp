from kivy.properties import StringProperty

from View.CreateScreen.components import SwipeItem
from View.base_screen import BaseScreenView


class CreateScreenView(BaseScreenView):
    """Class of the list of ingredients that the user can add"""
    cost = StringProperty()
    ingredient = StringProperty()

    def on_enter(self):
        if not self.ids.content.children:
            for key, value in self.model.ingredient.items():
                self.ids.content.add_widget(
                    SwipeItem(
                        source=value[1],
                        text=key,
                        cost=value[0],
                        controller=self.controller
                    )
                )

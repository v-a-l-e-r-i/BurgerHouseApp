from kivy.properties import NumericProperty

from View.PayScreen.components import SwipeToDeleteItem
from View.base_screen import BaseScreenView


class PayScreenView(BaseScreenView):
    cost = NumericProperty(0)

    def on_enter(self):
        """Function of filling in the list of products"""
        self.ids.md_list.clear_widgets()
        self.cost = 0
        for key in self.model.burgers:
            self.cost += key[1]
            self.ids.md_list.add_widget(
                SwipeToDeleteItem(
                    text=f"{key[0]}",
                    cost=f"{key[1]}",
                    ingredient = f"{key[2]}",
                    source=f"{key[3]}",
                    on_swipe_complete=self.controller.on_swipe_complete
                )
            )

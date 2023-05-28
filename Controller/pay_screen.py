
from View.PayScreen.pay_screen import PayScreenView


class PayScreenController:
    def __init__(self, model):
        self.model = model  # Model.pay_screen.PayScreenModel
        self.view = PayScreenView(controller=self, model=self.model)

    def on_tap_chevron(self):
        """Function that opens the main page"""
        self.view.manager_screens.current = "main screen"

    def on_swipe_complete(self, instance):
        """The function of removing an item from the cart"""

        #Delete the widget itself
        self.view.ids.md_list.remove_widget(instance)

        #Getting product data
        burger_name = instance.ids.content.text
        burger_cost = instance.ids.content_cost.text
        burger_ingredient = instance.ids.content_ingredient.text

        #Reducing the purchase amount
        self.view.cost -= int(burger_cost)

        #Delete a burger by name and ingredients
        for x in self.model.burgers:
            if x[0] == burger_name and x[2] == burger_ingredient:
                self.model.burgers.remove(x)
                break

    def get_view(self) -> PayScreenView:
        return self.view

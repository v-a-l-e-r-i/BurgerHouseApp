from Model.info_screen import InfoScreenModel
from View.MainScreen.main_screen import MainScreenView


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def open_info_screen(self, instance):
        """The function that opens the information window for the selected product checks
            in which group of goods the product is located, and transfers to the information feed
            its data from the dictionaries located in the module"""
        name = instance.ids.burger_name.text

        if name in self.model.burgers:
            cost = self.model.burgers[instance.ids.burger_name.text][0]
            ingredient = self.model.burgers[instance.ids.burger_name.text][1]
            source = self.model.burgers[instance.ids.burger_name.text][2]
            kcal = self.model.burgers[instance.ids.burger_name.text][3]
            InfoScreenModel().info(name, cost, ingredient, source, kcal)
            self.view.manager_screens.current = "info screen"
        elif name in self.model.sauces:
            cost = self.model.sauces[instance.ids.burger_name.text][0]
            ingredient = self.model.sauces[instance.ids.burger_name.text][1]
            source = self.model.sauces[instance.ids.burger_name.text][2]
            kcal = self.model.sauces[instance.ids.burger_name.text][3]
            InfoScreenModel().info(name, cost, ingredient, source, kcal)
            self.view.manager_screens.current = "info screen"
        elif name in self.model.drinks:
            cost = self.model.drinks[instance.ids.burger_name.text][0]
            ingredient = self.model.drinks[instance.ids.burger_name.text][1]
            source = self.model.drinks[instance.ids.burger_name.text][2]
            kcal = self.model.drinks[instance.ids.burger_name.text][3]
            InfoScreenModel().info(name, cost, ingredient, source, kcal)
            self.view.manager_screens.current = "info screen"
        elif name in self.model.sweets:
            cost = self.model.sweets[instance.ids.burger_name.text][0]
            ingredient = self.model.sweets[instance.ids.burger_name.text][1]
            source = self.model.sweets[instance.ids.burger_name.text][2]
            kcal = self.model.sweets[instance.ids.burger_name.text][3]
            InfoScreenModel().info(name, cost, ingredient, source, kcal)
            self.view.manager_screens.current = "info screen"


    def get_view(self) -> MainScreenView:
        return self.view

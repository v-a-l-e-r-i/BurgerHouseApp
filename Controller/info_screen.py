from Model.pay_screen import PayScreenModel
from View.InfoScreen.info_screen import InfoScreenView


class InfoScreenController:

    def __init__(self, model):
        self.model = model  # Model.info_screen.InfoScreenModel
        self.view = InfoScreenView(controller=self, model=self.model)

    def on_tap_chevron(self):
        """A function that returns to the main page and clears the list,
            that displays information about the product"""
        self.view.manager_screens.current = "main screen"
        self.model.information.clear()

    def add_to_cart(self):
        """The function of adding an item to the cart"""
        try:
            #We get the data contained in the variable
            name = self.model.information[0]
            ingredient = self.model.information[2]
            source = self.model.information[3]
            cost = self.model.information[1]

            #Transfer data to the modular product list
            PayScreenModel().add_product(name, cost, ingredient, source)
            self.model.show(f"{name} successfully added", "check-circle-outline", "green")
        except:
            self.model.show(f"{name} not added", "information", "red")

    def get_view(self) -> InfoScreenView:
        return self.view

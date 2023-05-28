from Model.base_model import BaseScreenModel
from View.PayScreen.components import CustomSnackbar
from kivy.core.window import Window


class PayScreenModel(BaseScreenModel):
    #List of products to buy
    burgers = []

    def add_product(self, burger_name, burger_cost, ingresient, source):
        """The function of filling in the list"""
        self.burgers.append([burger_name, burger_cost, ingresient, source])

    def check_cart(self, price: int):
        """A function that checks if the cart is not empty"""
        if price > 0:
            self.show(f"Покупка на суму {price} UAH. Успішна!", "check-circle-outline", "green")
        else:
            self.show("Будь ласка оберіть продукти", "alert-circle-outline", "red")

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = CustomSnackbar(
            text=f"{text}",
            icon=f"{icon}",
            snackbar_x="10dp",
            snackbar_y="10dp",
            bg_color=(.91, .91, .91, 1),
        )
        snackbar.size_hint_x = (
            Window.width - (snackbar.snackbar_x * 2)
        ) / Window.width
        snackbar.ids.icon.icon_color = f"{color}"
        snackbar.open()

from Model.base_model import BaseScreenModel
from View.CreateScreen.components import OwnCustomSnackbar
from kivy.core.window import Window


class CreateScreenModel(BaseScreenModel):
    ingredient_cost = .2
    burger_ingredients = ["Bun",]

    def __init__(self):
        #List of available ingredients
        self.ingredient = {
            'Beef Meat': ["4", "./View/CreateScreen/components/ingredient/beef.jfif"],
            'Bacon Slice': ["5", "./View/CreateScreen/components/ingredient/bacon.jfif"],
            'Chicken Meat': ["3", "./View/CreateScreen/components/ingredient/chicken.jfif"],
            'Fish': ["2", "./View/CreateScreen/components/ingredient/fish.jfif"],
            'Tomato Slice': ["1", "./View/CreateScreen/components/ingredient/tomato.jfif"],
            'Lettuce': [".5", "./View/CreateScreen/components/ingredient/lettuce.jfif"],
            'Onion Slice': [".5", "./View/CreateScreen/components/ingredient/onion.jpg"],
            'Cheese Slice': ["3", "./View/CreateScreen/components/ingredient/cheese.jpg"],
        }

        #Photo displayed in the shopping cart
        self.ingredient_source = "./View/CreateScreen/components/ingredient/your_burger.png"

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = OwnCustomSnackbar(
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
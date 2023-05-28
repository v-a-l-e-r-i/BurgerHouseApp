from Model.base_model import BaseScreenModel
from View.InfoScreen.components import AddCustomSnackbar
from kivy.core.window import Window


class InfoScreenModel(BaseScreenModel):
    #a list of information about the burger displayed on the screen
    information = []

    def info(self, name, cost, ingredient, source, kcal):
        """The function of filling in the list of information"""
        self.information.append(name)
        self.information.append(cost)
        self.information.append(ingredient)
        self.information.append(source)
        self.information.append(kcal)

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = AddCustomSnackbar(
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

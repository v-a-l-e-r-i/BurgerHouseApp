from kivy.properties import StringProperty, NumericProperty
from View.base_screen import BaseScreenView


class InfoScreenView(BaseScreenView):
    """A class that displays detailed information about the product"""

    #Properties displayed on the screen
    burger_name = StringProperty()
    ingredient = StringProperty()
    source = StringProperty()
    cost = NumericProperty()
    kcal = NumericProperty()

    def on_enter(self):
        """Function, display of product information"""
        self.burger_name = self.model.information[0]
        self.ingredient = self.model.information[2]
        self.source = self.model.information[3]
        self.cost = self.model.information[1]
        self.kcal = self.model.information[4]


    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

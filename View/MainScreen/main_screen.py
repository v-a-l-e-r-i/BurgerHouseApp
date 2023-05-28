from View.MainScreen.components import HeroCard
from View.base_screen import BaseScreenView


class MainScreenView(BaseScreenView):

    def on_enter(self):
        """Function of filling the list of products with components"""

        if not self.ids.burger_grid.children:
            for key, value in self.model.burgers.items():
                self.ids.burger_grid.add_widget(
                    HeroCard(
                        title=key,
                        source=value[2],
                        on_release=self.controller.open_info_screen,
                    )
                )

        if not self.ids.sauces_grid.children:
            for key, value in self.model.sauces.items():
                self.ids.sauces_grid.add_widget(
                    HeroCard(
                        title=key,
                        source=value[2],
                        on_release=self.controller.open_info_screen,
                    )
                )

        if not self.ids.sweets_grid.children:
            for key, value in self.model.sweets.items():
                self.ids.sweets_grid.add_widget(
                    HeroCard(
                        title=key,
                        source=value[2],
                        on_release=self.controller.open_info_screen,
                    )
                )

        if not self.ids.drinks_grid.children:
            for key, value in self.model.drinks.items():
                self.ids.drinks_grid.add_widget(
                    HeroCard(
                        title=key,
                        source=value[2],
                        on_release=self.controller.open_info_screen,
                    )
                )

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

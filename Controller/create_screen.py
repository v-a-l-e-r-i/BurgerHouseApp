from Model.pay_screen import PayScreenModel
from View.CreateScreen.create_screen import CreateScreenView


class CreateScreenController:
    def __init__(self, model):
        self.model = model  # Model.create_screen.CreateScreenModel
        self.view = CreateScreenView(controller=self, model=self.model)

        self.view.cost = str(self.model.ingredient_cost)
        self.view.ingredient = ", ".join(self.model.burger_ingredients)

    def on_tap_chevron(self):
        """Повертає до головної сторінки"""
        self.view.manager_screens.current = "main screen"

    def checking_the_product_limit(self, instance):
        """Перевіряє чи досягло добавлення продуктів ліміту
            Якщо досягло відображає повідомлення"""
        title = instance.ids.content.text
        cost = instance.ids.content_cost.text
        meat = ["Beef Meat", "Chicken Meat", "Fish"]

        if title not in meat:
            if len(self.model.burger_ingredients) < 15:
                self.model.ingredient_cost += float(cost)
                self.model.burger_ingredients.append(title)
                self.view.cost = str(round(self.model.ingredient_cost, 1))
                self.view.ingredient = ", ".join(self.model.burger_ingredients)
            else:
                self.model.show("Не можна добавити більше інгредієнтів", "information", "red")
        else:
            if self.isMeatEqualLimetedNumber():
                self.model.ingredient_cost += float(cost)
                self.model.burger_ingredients.append(title)
                self.view.cost = str(round(self.model.ingredient_cost, 1))
                self.view.ingredient = ", ".join(self.model.burger_ingredients)
            else:
                self.model.show("Не можна добавити більше м'яса", "information", "red")

    def isMeatEqualLimetedNumber(self):
        """Перевіряє чи кількість м'яса при добавленні не досягло ліміту"""
        k = 0
        for x in self.model.burger_ingredients:
            if x == "Beef Meat" or x == "Chicken Meat" or x == "Fish":
                k += 1
        if k >= 5:
            return False
        else:
            return True

    def add_your_to_cart(self):
        """A function that adds a burger to the cart and
            clears the list for added items."""
        try:

            #Adding a product to the list in the module
            PayScreenModel().add_product(
                "Your Burger",
                round(self.model.ingredient_cost),
                ', '.join(self.model.burger_ingredients),
                self.model.ingredient_source
            )
            self.model.show("Burger has been added to your cart!", "check-circle-outline", "green")

            #Returns to the original state of variables
            self.model.ingredient_cost = 0.2
            self.model.burger_ingredients = ["Bun",]

            #Changes the display on the screen
            self.view.cost = str(round(self.model.ingredient_cost, 1))
            self.view.ingredient = ", ".join(self.model.burger_ingredients)
        except:
            self.model.show("Your burger has not been added to the cart", "check-circle-outline", "green")

    def get_view(self) -> CreateScreenView:
        return self.view

from Model.base_model import BaseScreenModel
from Model.pay_screen import PayScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    def __init__(self):
        """Available products for purchase"""
        self.burgers = {
            "CheeseBurger": [
                25, "Bun, Beef Patty, Cheese Slice, Ketchup, Pickle Slices, Onions, Mustard",
                "./View/MainScreen/components/foto/burgers/cheeseburger.jfif", 303],
            "Hamburger": [
                15, "Bun, Beef Patty, Ketchup, Pickle Slices, Onions, Mustard",
                "./View/MainScreen/components/foto/burgers/hamburger.jfif", 295],
            "McDouble": [
                20, "Bun, Beef Patty, Cheese Slice, Ketchup, Pickle Slices, Onions, Mustard",
                "./View/MainScreen/components/foto/burgers/mcdouble.jfif", 400],
            "Double CheeseBurger": [
                31, "Bun, Double Beef Pattys, Double Cheese Slices, Ketchup, Pickle Slices, Onions, Mustard",
                "./View/MainScreen/components/foto/burgers/double-cheeseburger.jfif", 450],
            "Double Bacon": [
                27, "Bun, Bacon slice, Beef Patty, Cheese Slice, Crispy Onions, Pickle Slices",
                "./View/MainScreen/components/foto/burgers/double-bacon.jfif", 630],
        }
        self.sauces = {
            "Ketchup": [
                2, "",
                "./View/MainScreen/components/foto/sauces/ketchup.jfif", 10],
            "BBQ": [
                4, "",
                "./View/MainScreen/components/foto/sauces/bbq.jfif", 45],
            "Curry": [
                2, "",
                "./View/MainScreen/components/foto/sauces/curry.jfif", 47],
            "Honey": [
                3, "",
                "./View/MainScreen/components/foto/sauces/honey.jfif", 50],
            "Jam": [
                2, "",
                "./View/MainScreen/components/foto/sauces/jam.jfif", 40],
            "Sweet-Sour": [
                3, "",
                "./View/MainScreen/components/foto/sauces/sweet-sour.jfif", 50],
        }
        self.drinks = {
            "Coca-Cola": [
                3, "L",
                "./View/MainScreen/components/foto/drinks/cola.jfif", 290],
            "Sprite": [
                3, "L",
                "./View/MainScreen/components/foto/drinks/sprite.jfif", 230],
            "Fanta": [
                3, "L",
                "./View/MainScreen/components/foto/drinks/fanta.jfif", 300],
            "Sweet Tea": [
                2, "L",
                "./View/MainScreen/components/foto/drinks/sweet-tea.jfif", 170],
            "Orange Juice": [
                2, "L",
                "./View/MainScreen/components/foto/drinks/orange-juice.jfif", 270],
            "Water": [
                1, "L",
                "./View/MainScreen/components/foto/drinks/water.jfif", 0],
            "Lemonade": [
                2, "L",
                "./View/MainScreen/components/foto/drinks/lemonade.jfif", 320]
        }
        self.sweets = {
            "Apple Pie": [
                3, "Apples (apples, Ascorbic Acid, Salt, Citric Acid), Enriched Flour (bleached Wheat Flour, "
                   "Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Sugar, Palm Oil, Water, "
                   "Apple Juice Concentrate, Modified Food Starch, Invert Syrup, Contains 2% Or Less: Yeast, Salt, "
                   "Cinnamon, Sunflower Lecithin, L-cysteine (dough Conditioner), Yeast Extract, Enzyme, "
                   "Beta-carotene (color).",
                "./View/MainScreen/components/foto/sweets/apple-pie.jfif", 230],
            "McFlurry with OREO": [
                5, "Milk, Sugar, Cream, Corn Syrup, Natural Flavor, Mono And Diglycerides, Cellulose Gum, "
                   "Guar Gum, Carrageenan, Vitamin A Palmitate. Unbleached Enriched Flour (wheat Flour, "
                   "Niacin, Reduced Iron, Thiamine Mononitrate [vitamin B1], Riboflavin [vitamin B2], Folic Acid), "
                   "Sugar, Palm And/or Canola Oil, Cocoa (processed With Alkali), Invert Sugar, "
                   "Leavening (baking Soda And/or Calcium Phosphate), Soy Lecithin, Salt, Chocolate, Natural Flavor.",
                "./View/MainScreen/components/foto/sweets/oreo.jfif", 510],
            "McFlurry with M & M'S": [
                6, "Milk, Sugar, Cream, Corn Syrup, Natural Flavor, Mono And Diglycerides, Cellulose Gum, "
                   "Guar Gum, Carrageenan, Vitamin A Palmitate. Milk Chocolate "
                   "(Sugar, Chocolate, Skim Milk, Cocoa Butter, Lactose, Milkfat, Soy Lecithin, Salt, "
                   "Artificial And Natural Flavors), Sugar, Contains 2%",
                "./View/MainScreen/components/foto/sweets/m&ms.jfif", 640],
            "Vanilla Cone": [
                2, "Milk, Sugar, Cream, Corn Syrup, Natural Flavor, Mono And Diglycerides, Cellulose Gum, "
                   "Guar Gum, Carrageenan, Vitamin A Palmitate. Enriched Wheat Flour (Wheat Flour, Niacin, "
                   "Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Tapioca Starch, Sugar, "
                   "Contains 2%",
                "./View/MainScreen/components/foto/sweets/vanila.jfif", 200],
            "Hot Fudge Sundae": [
                3, "Milk, Sugar, Cream, Corn Syrup, Natural Flavor, Mono And Diglycerides, Cellulose Gum, "
                   "Guar Gum, Carrageenan, Vitamin A Palmitate. Sugar, Water, Nonfat Milk, "
                   "Hydrogenated Palm Kernel Oil, Cocoa (processed With Alkali), Corn Syrup, Salt, "
                   "Disodium Phosphate, Soy Lecithin, Natural Flavor, Potassium Sorbate (preservative), "
                   "Polyglycerol Esters Of Fatty Acids.",
                "./View/MainScreen/components/foto/sweets/fudge.jfif", 330],
            "Hot Caramel Sundae": [
                3, " Milk, Sugar, Cream, Corn Syrup, Natural Flavor, Mono And Diglycerides, Cellulose Gum, "
                   "Guar Gum, Carrageenan, Vitamin A Palmitate. Corn Syrup, Milk, Sugar, High Fructose Corn "
                   "Syrup, Water, Butter (cream, Salt), Disodium Phosphate, Salt, Pectin, Natural Flavor.",
                "./View/MainScreen/components/foto/sweets/caramel.jfif", 330],
            "Chocolate Chip Cookie": [
                2, "Semi-sweet Chocolate Chips (sugar, Unsweetened Chocolate, Cocoa Butter, Milkfat, "
                   "Soy Lecithin, Natural Flavor), Enriched Flour (bleached Wheat Flour, Malted Barley Flour, "
                   "Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Margarine (palm Oil, Water, "
                   "Soybean Oil, Salt, Whey, Natural Flavor, Mono And Diglycerides, Soy Lecithin, Vitamin A Palmitate, "
                   "Beta Carotene [color]), Sugar, Brown Sugar, Egg, Contains 2%",
                "./View/MainScreen/components/foto/sweets/cookie.jfif", 170]
        }
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCardSwipe


class SwipeToDeleteItem(MDCardSwipe):
    """Component that fills the product list"""
    cost = StringProperty()
    text = StringProperty()
    ingredient = StringProperty()
    source = StringProperty()

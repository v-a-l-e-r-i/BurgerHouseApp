from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.card import MDCard


class SwipeItem(MDCard):
    """The class responsible for the appearance of each
        component of the ingredient list"""
    controller = ObjectProperty()
    cost = StringProperty()
    text = StringProperty()
    source = StringProperty()




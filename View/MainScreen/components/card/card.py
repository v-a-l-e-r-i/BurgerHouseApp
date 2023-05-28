from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard


class ElevationCard(FakeRectangularElevationBehavior, MDCard):
    pass


class HeroCard(ElevationCard):
    """Components of the list of available products"""
    title = StringProperty()
    source = StringProperty()
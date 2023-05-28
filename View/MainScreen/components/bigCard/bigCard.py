from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard


class ElevationBigCard(FakeRectangularElevationBehavior, MDCard):
    pass


class BigCard(ElevationBigCard):
    source = StringProperty("./View/MainScreen/components/foto/logo.png")
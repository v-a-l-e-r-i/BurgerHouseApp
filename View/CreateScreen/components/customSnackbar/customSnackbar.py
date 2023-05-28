from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.snackbar import BaseSnackbar


class OwnCustomSnackbar(BaseSnackbar):
    """The class that is responsible for the notification window"""
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
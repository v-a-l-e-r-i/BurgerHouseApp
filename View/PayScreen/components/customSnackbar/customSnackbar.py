from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.snackbar import BaseSnackbar


class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
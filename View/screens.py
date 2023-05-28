# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.info_screen import InfoScreenModel
from Controller.info_screen import InfoScreenController
from Model.create_screen import CreateScreenModel
from Controller.create_screen import CreateScreenController
from Model.pay_screen import PayScreenModel
from Controller.pay_screen import PayScreenController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "info screen": {
        "model": InfoScreenModel,
        "controller": InfoScreenController,
    },

    "create screen": {
        "model": CreateScreenModel,
        "controller": CreateScreenController,
    },

    "pay screen": {
        "model": PayScreenModel,
        "controller": PayScreenController,
    },
}
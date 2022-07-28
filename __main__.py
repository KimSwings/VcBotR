from ubb import Ubot
from ubb.modules import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("ubb.modules." + module_name)

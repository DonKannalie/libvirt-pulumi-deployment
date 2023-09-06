import importlib
import os

networks = {}

test = importlib.import_module(".bridges", __name__)
print(test)
import pulumi
import importlib

config = importlib.import_module(f'.{pulumi.get_stack()}.vars', __name__)
globals().update(vars(config))
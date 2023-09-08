import pulumi
import importlib

config_items = [
    'providers',
    'networks',
    'base_images',
    'volumes',
    'vms'
]

config = importlib.import_module(f'.{pulumi.get_stack()}.vars', __name__)
globals().update({key:vars(config).get(key) for key in config_items})
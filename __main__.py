"""A Python Pulumi program"""
from common import module_iterator

submodules = [
    {'name': 'providers', 'blacklist': ['util']},
    {'name': 'networks', 'blacklist': ['util']},
    {'name': 'base_images', 'blacklist': ['util']},
    {'name': 'volumes', 'blacklist': ['util']},
    {'name': 'vms', 'blacklist': ['util']},
]

for submodule in submodules:
    for mod in module_iterator(submodule['name'], submodule['blacklist']):
        mod.run()
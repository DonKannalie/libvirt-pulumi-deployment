"""A Python Pulumi program"""
import config
from common import module_iterator

for submodule in config.submodules:
    for mod in module_iterator(submodule['name'], submodule['blacklist']):
        mod.run()
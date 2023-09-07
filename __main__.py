"""A Python Pulumi program"""
import vars
from common import module_iterator

for submodule in vars.submodules:
    for mod in module_iterator(submodule['name'], submodule['blacklist']):
        mod.run(None)
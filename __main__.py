"""A Python Pulumi program"""

import pulumi
import os
import importlib
import pulumi_libvirt as libvirt
from common.common import module_iterator

from vars import *

providers = {}

for host in hosts:
    providers.update({host['name']: libvirt.Provider(resource_name = host['name'], uri = host['uri'])})

for submodule in submodules:
    for mod in module_iterator(submodule):
        mod.run(providers)
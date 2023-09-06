from common import module_iterator
import vars

def get_networks():
    networks = []
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        networks.append(mod.networks)
    return networks
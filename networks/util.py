from common import module_iterator

def get_networks():
    networks = {}
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        networks.update(mod.networks)
    return networks

def get_network(name):
    print(get_networks())
    return get_networks()[name]
from common import module_iterator

def get_volumes():
    volumes = {}
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        volumes.update(mod.volumes)
    return volumes

def get_volume(name):
    return get_volumes()[name]
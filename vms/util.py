from common import module_iterator

def get_vms():
    vms = {}
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        vms.update(mod.vms)
    return vms

def get_vm(name):
    return get_vms()[name]
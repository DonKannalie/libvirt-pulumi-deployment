from common import module_iterator

def get_providers():
    providers = {}
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        providers.update(mod.providers)
    return providers

def get_provider(name: str):
    return get_providers()[name]
import vars
import pulumi

from pulumi_libvirt import Provider

providers = {}

def run(hosts):
    global providers
    for provider in vars.providers:
        new_provider = Provider(resource_name = provider['name'], uri = provider['uri'])
        providers.update({ provider['name']: new_provider })
        pulumi.export(provider['name'], new_provider)



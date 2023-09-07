import vars
import pulumi

from pulumi_libvirt import Provider

providers = {}

def run(hosts):
    global providers
    for provider in vars.providers:
        providers.update({provider['name']: Provider(resource_name = provider['name'], uri = provider['uri'])})



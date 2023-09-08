import config
import pulumi

from pulumi_libvirt import Network
from providers import get_provider

networks = {}

def run():
    global networks

    for network in config.networks:
        for host in network['hosts']:
            if network['mode'] == 'bridge':
                new_network = Network(resource_name=f"{network['name']}_{host}",
                                mode=network['mode'],
                                bridge=network['bridge'],
                                autostart=network['autostart'],
                                opts=pulumi.ResourceOptions(provider=get_provider(host)))
            else:
                new_network = Network(resource_name=f"{network['name']}_{host}",
                                mode=network['mode'],
                                autostart=network['autostart'],
                                opts=pulumi.ResourceOptions(provider=get_provider(host)))
            networks.update({f"{network['name']}_{host}": new_network})
            pulumi.export(f"{network['name']}_{host}", new_network)
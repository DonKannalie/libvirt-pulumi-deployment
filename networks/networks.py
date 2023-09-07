import vars
import pulumi

from pulumi_libvirt import Network
from providers import get_provider

networks = {}

def run(hosts):
    global networks

    for network in vars.networks:
        for host in network['hosts']:
            if network['mode'] == 'bridge':
                new_network = {f"{network['name']}_{host}":
                    Network(resource_name=f"{network['name']}_{host}",
                            mode=network['mode'],
                            bridge=network['bridge'],
                            autostart=network['autostart'],
                            opts=pulumi.ResourceOptions(provider=get_provider(host)))}
            else:
                new_network = {f"{network['name']}_{host}":
                    Network(resource_name=f"{network['name']}_{host}",
                            mode=network['mode'],
                            autostart=network['autostart'],
                            opts=pulumi.ResourceOptions(provider=get_provider(host)))}
            networks.update(new_network)
            pulumi.export(f"{network['name']}_{host}", new_network)
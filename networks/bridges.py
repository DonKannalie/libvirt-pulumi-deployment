import pulumi
from pulumi_libvirt import Network


networks = {}

def run(hosts):
    global networks

    for key, value in hosts.items():
        networks.update({f"bridge_network_{key}":
                         Network(resource_name=f"bridge_network_{key}",
                                mode='bridge',
                                bridge='br0',
                                autostart=True,
                                opts=pulumi.ResourceOptions(provider=value))})
        # pulumi.export(f"bridge_network_{key}", networks[f"bridge_network_{key}"])
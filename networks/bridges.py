from pulumi import ResourceOptions
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
                                opts=ResourceOptions(provider=value))})
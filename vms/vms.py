import vars
import pulumi

from pulumi_libvirt import Domain
from providers import get_provider
from volumes import get_volume, get_volumes
from networks import get_network, get_networks
from cloudinit import create_cloudinit_disk

vms = {}

def run():
    global vms

    for vm in vars.vms:
        user_data = vm['cloudinit']['user_data'] if vm['cloudinit']['user_data'] else {}
        meta_data = vm['cloudinit']['meta_data'] if vm['cloudinit']['meta_data'] else {}

        cloudinit_disk = create_cloudinit_disk(f"{vm['name']}-cloudinit",
                                               provider=get_provider(vm['libvirt_host']),
                                               user_data=user_data,
                                               meta_data=meta_data)

        new_vm = Domain(resource_name=f"{vm['name']}-{vm['libvirt_host']}",
                        disks=[{'volume_id': get_volume(volume).id} for volume in vm['volumes'] if volume in get_volumes().keys() ],
                        network_interfaces=[{'network_id': get_network(f"{network}_{vm['libvirt_host']}").id} for network in vm['networks'] if f"{network}_{vm['libvirt_host']}" in get_networks().keys() ],
                        memory=vm['memory'],
                        vcpu=vm['vcpu'],
                        graphics = {'type': 'vnc', 'listen_type': 'address'},
                        cpu={'mode': 'host-passthrough'},
                        cloudinit= cloudinit_disk.id,
                        opts=pulumi.ResourceOptions(provider=get_provider(vm['libvirt_host']),
                                                    depends_on= [cloudinit_disk] +
                                                                [ get_volume(volume) for volume in vm['volumes'] if volume in get_volumes().keys() ]+
                                                                [ get_network(f"{network}_{vm['libvirt_host']}") for network in vm['networks'] if f"{network}_{vm['libvirt_host']}" in get_networks().keys() ],
                                                    delete_before_replace=True)
                )

        vms.update({f"{vm['name']}-{vm['libvirt_host']}": new_vm})
        pulumi.export(f"{vm['name']}-{vm['libvirt_host']}", new_vm)

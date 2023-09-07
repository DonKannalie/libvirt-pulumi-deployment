import pulumi
import pulumi_libvirt
import networks
import base_images


from cloudinit import create_cloudinit_disk

libvirt_host = "virt01"

def run(hosts):
    cloudinit_disk = create_cloudinit_disk(f'{__name__}-cloudinit', provider=hosts[libvirt_host])

    vm_name = f'{__name__}-{libvirt_host}-vm'
    vm = pulumi_libvirt.Domain(resource_name=vm_name,
                               disks= [{
                                   'volume_id': vol.id
                               }],
                               memory = 4096,
                               vcpu = 4,
                               graphics = {
                                 'type': 'vnc',
                                 'listen_type': 'address'
                               },
                               cpu={
                                 'mode': 'host-passthrough'
                               },
                               cloudinit= cloudinit_disk.id,
                               network_interfaces = [{
                                   'network_id': networks.get_networks()[f'bridge_network_{libvirt_host}']
                               }],
                               opts=pulumi.ResourceOptions(provider=hosts[libvirt_host],
                                                           depends_on=[ vol, cloudinit_disk ],
                                                           delete_before_replace=True))
    pulumi.export(vm_name, vm)

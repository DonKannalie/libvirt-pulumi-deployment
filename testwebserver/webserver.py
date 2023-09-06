import pulumi
import pulumi_libvirt
import networks
import base_images

libvirt_host = "virt01"

def run(hosts):
    volume_name = f'{__name__}-{libvirt_host}-vol'
    vol = pulumi_libvirt.Volume(resource_name=volume_name,
                                size = 1024*1024*1024*20,
                                base_volume_id=base_images.get_images()['almalinux'].id,
                                opts=pulumi.ResourceOptions(provider=hosts[libvirt_host],
                                                            depends_on=base_images.get_images()['almalinux']))
    pulumi.export(volume_name, vol)

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
                               network_interfaces = [{
                                   'network_id': networks.get_networks()[f'bridge_network_{libvirt_host}']
                               }],
                               opts=pulumi.ResourceOptions(provider=hosts[libvirt_host],
                                                           depends_on=vol,
                                                           delete_before_replace=True))
    pulumi.export(vm_name, vm)

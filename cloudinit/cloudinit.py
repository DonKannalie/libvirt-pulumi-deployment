import pulumi
from pulumi_libvirt import CloudInitDisk
from template_renderer import render_template

def create_cloudinit_disk(name: str, provider: pulumi.ProviderResource ,user_data: dict = {}, meta_data: dict = {}, network_config= {}):
    cloudinit_disk_name = f'{name}-cloudinit-disk'
    cloudinit_disk = CloudInitDisk(
        resource_name=cloudinit_disk_name,
        name=f"{cloudinit_disk_name}.iso",
        user_data=render_template('cloudinit/user_data.j2', user_data),
        meta_data=render_template('cloudinit/meta_data.j2', meta_data),
        network_config=render_template('cloudinit/network_config.j2', network_config),
        opts=pulumi.ResourceOptions(provider=provider)
    )
    pulumi.export(f'{name}-cloudinit-disk', cloudinit_disk)

    return cloudinit_disk
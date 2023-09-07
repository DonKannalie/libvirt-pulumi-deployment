import vars
import pulumi

from pulumi_libvirt import Volume
from base_images import get_image
from providers import get_provider

volumes = {}

def run():
    global volumes

    for volume in vars.volumes:
        new_volume = {}
        if volume['base_image']:
            new_volume = Volume(resource_name=f"{volume['name']}-{volume['host']}-vol",
                                size=volume['size'],
                                base_volume_id=get_image(volume['base_image']).id,
                                opts=pulumi.ResourceOptions(provider=get_provider(volume['host']),
                                        depends_on=get_image(volume['base_image'])))
        else:
            new_volume = Volume(resource_name=f"{volume['name']}-{volume['host']}",
                                size=volume['size'],
                                opts=pulumi.ResourceOptions(provider=get_provider(volume['host'])))
        volumes.update({volume['name']: new_volume})
        pulumi.export(f"{volume['name']}-vol", new_volume)
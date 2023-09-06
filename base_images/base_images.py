import pulumi
import pulumi_libvirt
import vars

images = {}

def run(hosts):
    global images
    for image in vars.base_images:
        new_image = pulumi_libvirt.Volume(resource_name=f"{image['name']}",
                              source=f"{image['url']}",
                              opts=pulumi.ResourceOptions(provider=list(hosts.values())[0]))
        images.update({f"{image['name']}": new_image})
        pulumi.export(f"{image['name']}", new_image)
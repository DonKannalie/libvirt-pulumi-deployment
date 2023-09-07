from common import module_iterator

def get_images():
    images = {}
    for mod in module_iterator(__name__.split('.')[0], ['util']):
        images.update(mod.images)
    return images

def get_image(name):
    return get_images()[name]
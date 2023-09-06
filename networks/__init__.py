from common import module_iterator

networks = {}

for mod in module_iterator(__name__):
    print(mod)
providers = [
    {
        'name': 'virt01',
        'uri': 'qemu+ssh://virtmgr@192.168.5.31/system?keyfile=/home/sfenzke/.ssh/virtmgr&sshauth=privkey&no_verify=1'
    },
    {
        'name': 'virt02',
        'uri': 'qemu+ssh://virtmgr@192.168.5.32/system?keyfile=/home/sfenzke/.ssh/virtmgr&sshauth=privkey&no_verify=1'
    }
]

submodules = [
    {'name': 'providers', 'blacklist': ['util']},
    {'name': 'networks', 'blacklist': ['util']},
    {'name': 'base_images', 'blacklist': ['util']},
     {'name': 'volumes', 'blacklist': ['util']},
    # {'name': 'testwebserver', 'blacklist': []}
]

networks = [
    {
        'name': "bridge_network",
        'mode': 'bridge',
        'bridge': 'br0',
        'autostart': 'true',
        'hosts': [ 'virt01', 'virt02' ]
    },
]

base_images = [
    {'name': "almalinux",
     'url': 'https://repo.almalinux.org/almalinux/9/cloud/x86_64/images/AlmaLinux-9-GenericCloud-9.2-20230513.x86_64.qcow2'
    }
]

volumes = [
    {
        'name': 'testwebserver',
        'base_image': 'almalinux',
        'size': 1024*1024*1024*10,
        'host': 'virt01'
    }
]

vms = [
    {
        'name': 'testwebserver',
        'libvirt_host': 'virt01',
        'vcpus': 4,
        'memory': 2048,
        'volumes': [
            'testwebserver'
        ],
        'network_interfaces': [
            'bridge_network'
        ],
        'cloudinit': {
            'user_data': {},
            'meta_data': {}
        }
    }
]
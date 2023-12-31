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
        'name': 'testserver',
        'base_image': 'almalinux',
        'size': 1024*1024*1024*10,
        'host': 'virt01'
    }
]

vms = [
    {
        'name': 'testserver',
        'libvirt_host': 'virt01',
        'vcpu': 4,
        'memory': 2048,
        'volumes': [
            'testserver'
        ],
        'networks': [
            'bridge_network'
        ],
        'cloudinit': {
            'user_data': {
                'default_passwd': "sagichnicht",
                # 'users': [
                #     {
                #         'name': 'testuser',
                #         'sudo': 'ALL=(ALL) NOPASSWD:ALL'
                #     }
                # ]
            },
            'meta_data': {
                'hostname': 'testserver'
            },
            'network_config': {}
        }
    }
]
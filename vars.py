hosts = [
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
    {'name': 'networks', 'blacklist': ['util']},
    {'name': 'base_images', 'blacklist': ['util']},
    {'name': 'testwebserver', 'blacklist': []}
]

base_images = [
    {'name': "almalinux", 'url': 'https://repo.almalinux.org/almalinux/9/cloud/x86_64/images/AlmaLinux-9-GenericCloud-9.2-20230513.x86_64.qcow2'}
]
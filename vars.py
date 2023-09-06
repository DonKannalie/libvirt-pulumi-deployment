hosts = [
    {
        'name': 'virt01',
        'uri': 'qemu+ssh://virtmgr@192.168.5.31/system?keyfile=/home/sfenzke/.ssh/virtmgr&sshauth=privkey&no_verify=1'
    },
    {
        'name': 'virt02',
        'uri': 'qemu+ssh://virtmgr@192.168.5.31/system?keyfile=/home/sfenzke/.ssh/virtmgr&sshauth=privkey&no_verify=1'
    }
]

submodules = [
    'networks'
]

stackhpc.sriov
==============

Ansible role to enable SR-IOV. Currently only mellanox cards are supported.

Requirements
------------

The following programs:

- `lshw`

The following pip packages:

- `xmltodict` (FIXME: use sysfs instead of lshw)
- `lxml`
- `jmespath`

Role Variables
--------------

See `defaults/main.yml`

Dependencies
------------

- `stackhpc.grubcmdline`

Example Playbook
----------------

```
- name: configure sr-iov
  hosts: compute
  vars:
    sriov_devices:
      - p4p1
  tasks:
    - include_role:
        name: sriov
  handlers:
    - name: reboot
      include_tasks: tasks/reboot.yml
```

License
-------

Apache

Author Information
------------------

Will Szumski

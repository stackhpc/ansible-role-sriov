stackhpc.sriov
==============

[![Build Status](https://travis-ci.com/stackhpc/ansible-role-sriov.svg?branch=master)](https://travis-ci.com/stackhpc/ansible-role-sriov)

Ansible role to enable SR-IOV on network devices.

Requirements
------------
None

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
      - name: p4p1
        numvfs: 63
  tasks:
    - include_role:
        name: sriov
  handlers:
    - name: reboot
      include_tasks: tasks/reboot.yml
```

License
-------

Apache2

Author Information
------------------

Will Szumski

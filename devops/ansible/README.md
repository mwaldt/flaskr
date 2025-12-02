# Ansible

Quick example of running a basic program with ansible. Based on this tutorial:
https://docs.ansible.com/projects/ansible/latest/getting_started/index.html

## Getting started

1. `mkdir ansible_quickstart && cd ansible_quickstart`
1. Using a system python `python -m venv venv`
1. install ansbile `venv/bin/pip install ansible`

## Building an Inventory

You will need some hosts here, virtual machines are fine. Make sure your SSH key is loaded onto these machines in the `authorized_keys` file.


1. Create a `echo "[myhosts]"` >> inventory.ini` file and directory created above `ansible_quickstart`
1. Edit the `inventory.ini` file and add the IPV4 Addresses of your hosts, each on its own line
```
[myhosts]
192.0.2.50
192.0.2.51
192.0.2.52
```
1. Validate the inventory `venv/bin/ansible-inventory -i inventory.ini --list`
1. Ping the hosts in your inventory `venv/bin/ansible myhosts -m ping -i inventory.ini`


## Create a playbook

1.  Create a file named `playbook.yaml` inthe `ansible_quickstart` directory
```
- name: My first play
  hosts: myhosts
  tasks:
   - name: Ping my hosts
     ansible.builtin.ping:

   - name: Print message
     ansible.builtin.debug:
       msg: Hello world
```
1. Run the playbook with
```
venv/bin/ansible-playbook -i inventory.ini playbook.yaml
```

And with that you ran ansible!

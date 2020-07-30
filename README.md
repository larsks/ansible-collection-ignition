# Ansible Collection - larsks.ignition

This collection provides the `ignition_encode` filter, which will encode files for use in the `contents` key of an [Ignition][] `file` specification.

[ignition]: https://github.com/coreos/ignition

The filter was designed primarily for use when creating new
[MachineConfiguration][] objects when using the [k8s][] module.
You can use it in combination with Ansible's [lookup][] function to
include the content of files in your `MachineConfiguration` resources.

[lookup]: https://docs.ansible.com/ansible/latest/plugins/lookup.html
[machineconfiguration]: https://github.com/openshift/machine-config-operator
[k8s]: https://docs.ansible.com/ansible/latest/modules/k8s_module.html

## Example usage

```
- name: create an example file on worker nodes
  k8s:
    state: present
    definition:
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfig
      metadata:
        name: 50-example-file
        labels:
          machineconfiguration.openshift.io/role: worker
      spec:
        config:
          ignition:
            version: 2.2.0
          storage:
            files:
              - filesystem: root
                path: /etc/example-file
                contents:
                  source: "{{ lookup('file', 'example-file') | ignition_encode }}"
                mode: 0644
```

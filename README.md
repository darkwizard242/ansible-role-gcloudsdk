[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-gcloudsdk.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-gcloudsdk) ![Ansible Role](https://img.shields.io/ansible/role/46026?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/46026?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/46026?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-gcloudsdk&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-gcloudsdk) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-gcloudsdk?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-gcloudsdk?color=orange&style=flat-square)

# Ansible Role: gcloudsdk

Role to install (_by default_) `google-cloud-sdk` package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
gcloudsdk_pre_reqs_debian:
  - apt-transport-https
  - ca-certificates
  - lsb-release
  - gnupg
gcloudsdk_pre_reqs_debian_desired_state: present
gcloudsdk_app_name: google-cloud-sdk
gcloudsdk_desired_state: present
gcloudsdk_debian_gpg_key: https://packages.cloud.google.com/apt/doc/apt-key.gpg
gcloudsdk_repo_debian: "deb https://packages.cloud.google.com/apt cloud-sdk main"
gcloudsdk_repo_debian_filename: "{{ gcloudsdk_app_name }}"
gcloudsdk_el_gpg_yum_key: https://packages.cloud.google.com/yum/doc/yum-key.gpg
gcloudsdk_el_gpg_rpm_key: https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
gcloudsdk_repo_el_name: google-cloud-sdk
gcloudsdk_repo_el_description: Google Cloud SDK
gcloudsdk_repo_el: https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
gcloudsdk_repo_el_filename: "{{ gcloudsdk_app_name }}"
gcloudsdk_repo_el_repogpgcheck: yes
gcloudsdk_repo_el_gpgcheck: yes
gcloudsdk_repo_el_enabled: yes
gcloudsdk_repo_desired_state: present
```

### Variables table:

Variable                                | Value (default)                                                    | Description
--------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
gcloudsdk_pre_reqs_debian               | apt-transport-https, ca-certificates, lsb-release, gnupg           | Package required by Azure CLI on Debain based systems.
gcloudsdk_pre_reqs_debian_desired_state | present                                                            | State of the gcloudsdk_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
gcloudsdk_app_name                      | google-cloud-sdk                                                   | Name of Azure CLI package i.e. `google-cloud-sdk`
gcloudsdk_desired_state                 | present                                                            | State of the gcloudsdk_app_name package (i.e. `google-cloud-sdk` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
gcloudsdk_debian_gpg_key                | <https://packages.cloud.google.com/apt/doc/apt-key.gpg>            | Azure CLI GPG required on Debian based systems.
gcloudsdk_el_gpg_yum_key                | <https://packages.cloud.google.com/yum/doc/yum-key.gpg>            | Azure CLI GPG (yum) required on EL based systems.
gcloudsdk_el_gpg_rpm_key                | <https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg>    | Azure CLI GPG (rpm) required on EL based systems.
gcloudsdk_repo_debian                   | deb <https://packages.cloud.google.com/apt> cloud-sdk main         | Repository URL for Debian based systems.
gcloudsdk_repo_debian_filename          | "{{ gcloudsdk_app_name }}"                                         | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ gcloudsdk_app_name }}" which is `google-cloud-sdk` .
gcloudsdk_repo_el_name                  | google-cloud-sdk                                                   | Repository name for Azure CLI on EL based systems.
gcloudsdk_repo_el_description           | Google Cloud SDK                                                   | Description to be added in EL based repository file for Azure CLI.
gcloudsdk_repo_el                       | <https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64> | Repository `baseurl` for Azure CLI on EL based systems.
gcloudsdk_repo_el_repogpgcheck          | yes                                                                | Boolean operation for performing gpg check against atom's repository gpg. Can either be **yes** or **no**.
gcloudsdk_repo_el_gpgcheck              | yes                                                                | Boolean for whether to perform gpg check against Azure CLI on EL based systems.
gcloudsdk_repo_el_enabled               | yes                                                                | Boolean for whether to set Azure CLI repo as 'enabled' on EL based systems.
gcloudsdk_repo_desired_state            | present                                                            | `present` indicates creating the repository file if it doesn't exist on Debian or EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **google-cloud-sdk** pacakge).
gcloudsdk_repo_el_filename              | "{{ gcloudsdk_app_name }}"                                         | Name of the repository file that will be stored at `/etc/yum/sources.list.d/` on EL based systems. Defaults to the variable value for "{{ gcloudsdk_app_name }}" which is `google-cloud-sdk` .

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **google-cloud-sdk** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.gcloudsdk
```

For customizing behavior of role (i.e. installation of latest **google-cloud-sdk** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.gcloudsdk
      vars:
        gcloudsdk_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **google-cloud-sdk** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.gcloudsdk
      vars:
        gcloudsdk_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-gcloudsdk/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).

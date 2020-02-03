import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_gcloudsdk_repofile_exists(host):
    assert host.file('/etc/apt/sources.list.d/google-cloud-sdk.list').exists \
      or host.file('/etc/yum.repos.d/google-cloud-sdk.repo').exists


def test_gcloudsdk_repofile_isfile(host):
    assert host.file('/etc/apt/sources.list.d/google-cloud-sdk.list').is_file \
      or host.file('/etc/yum.repos.d/google-cloud-sdk.repo').is_file


def test_gcloudsdk_package_installed(host):
    assert host.package("google-cloud-sdk").is_installed


def test_gcloudsdk_binary_exists(host):
    host.file('/usr/bin/gcloud').exists


def test_gcloudsdk_binary_isfile(host):
    assert host.file('/usr/bin/gcloud').is_file


def test_gcloudsdk_binary_which(host):
    assert host.check_output('which gcloud') == '/usr/bin/gcloud'

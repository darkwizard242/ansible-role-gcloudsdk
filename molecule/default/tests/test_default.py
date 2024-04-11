import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'google-cloud-cli'
PACKAGE_BINARY = '/usr/bin/gcloud'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/google-cloud-sdk.list'
EL_REPO_FILE = '/etc/yum.repos.d/google-cloud-sdk.repo'


def test_gcloudsdk_package_installed(host):
    """
    Tests if google-cloud-sdk package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_gcloudsdk_binary_exists(host):
    """
    Tests if gcloud binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_gcloudsdk_binary_isfile(host):
    """
    Tests if gcloud binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_gcloudsdk_binary_which(host):
    """
    Tests the output to confirm gcloud's binary location.
    """
    assert host.check_output('which gcloud') == PACKAGE_BINARY


def test_gcloudsdk_repofile_exists(host):
    """
    Tests if repo file exists on Debian/EL based systems.
    """
    assert host.file(DEBIAN_REPO_FILE).exists \
        or host.file(EL_REPO_FILE).exists


def test_gcloudsdk_repofile_isfile(host):
    """
    Tests if repo file is a file type on Debian/EL based systems.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file \
        or host.file(EL_REPO_FILE).is_file

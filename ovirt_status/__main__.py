from json import loads, load
from os import environ

from requests import get
from requests_kerberos import HTTPKerberosAuth

with open('config.json') as config_file:
    config = load(config_file)

environ['REQUESTS_CA_BUNDLE'] = config['ca_bundle']


def main():
    with get(f"https://rhevm.abc.idm.lab.eng.brq.redhat.com/ovirt-engine/api/vms/{config['machine_id']}/statistics",
             auth=HTTPKerberosAuth(), headers={'accept': 'application/json'}) as response:
        if response.ok:
            result = loads(response.text)
        else:
            return False


if __name__ == '__main__':
    main()

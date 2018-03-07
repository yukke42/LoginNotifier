import argparse
import json
import sys

import requests
import yaml

with open('config.yml') as f:
    config = yaml.load(f)

WEBHOOK_URL = config['webhook_url']
IGNORE_IP_LIST = config.get('ignore_ip_list', [])


def get_hostip():
    resp = requests.get('http://inet-ip.info/ip')
    return resp.content.decode()


def notify():
    user = sys.argv[1]
    client_ip = sys.argv[2].split(' ')[0]
    host_ip = get_hostip()

    if client_ip in IGNORE_IP_LIST:
        return

    data = {
        'username':
        'LoginNotifier',
        'text':
        '<!channel> {} から {} に ユーザー {} でログインしました！'.format(
            client_ip, host_ip, user)
    }
    requests.post(WEBHOOK_URL, data=json.dumps(data))


if __name__ == '__main__':
    notify()

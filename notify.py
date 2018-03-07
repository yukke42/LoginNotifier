import argparse
import json
import sys

import requests
import yaml


def get_hostip():
    resp = requests.get('http://inet-ip.info/ip')
    return resp.content.decode()


def notify(url):
    user = sys.argv[1]
    client_ip = sys.argv[2].split(' ')[0]
    host_ip = get_hostip()
    data = {
        'username':
        'LoginNotifier',
        'text':
        '<!channel> {} から {} に ユーザー {} でログインしました！'.format(
            client_ip, host_ip, user)
    }
    requests.post(url, data=json.dumps(data))


def main():
    with open('config.yml', 'r') as f:
        config = yaml.load(f)

    webhook_url = config['webhook_url']
    notify(webhook_url)


if __name__ == '__main__':
    main()

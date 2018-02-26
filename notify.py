import requests, json, yaml, sys, argparse


def get_hostip():
    resp = requests.get('http://inet-ip.info/ip')
    return resp.content.decode()

def notify(url):
    user = sys.argv[2]
    client_ip = sys.argv[3].split(' ')[0]
    host_ip = get_hostip()
    data = {
        'username': 'LoginNotifier',
        'text': '{} から {} に ユーザー {} でログインしました！'.format(client_ip, host_ip, user)
    }
    requests.post(url, data=json.dumps(data))


def main():
    with open(sys.argv[1] + '/config.yml', 'r') as f:
        config = yaml.load(f)

    webhook_url = config['webhook_url']
    notify(webhook_url)


if __name__ == '__main__':
    main()

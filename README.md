# LoginNotifier

サーバーにSSHログインがあった際にSlackに通知する。


# Settings

環境設定
```
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ sudo sh -c "echo 'cd $PWD && bin/python notify.py \$USER \$SSH_CLIENT' > /etc/ssh/sshrc"
$ deactivate
```

[https://slack.com/services/new/incoming-webhook](https://slack.com/services/new/incoming-webhook) から Webhook URL を取得し

```
# config.yml
webhook_url: https://hooks.slack.com/services/xxxx
```

と設定する。


# LoginNotifier

サーバーにSSHログインがあった際にSlackに通知する。


# Settings

環境設定
```
$ pipenv install
$ sudo sh -c "echo 'cd $PWD && .venv/bin/python notify.py \$USER \$SSH_CLIENT' >> /etc/ssh/sshrc"
```

[https://slack.com/services/new/incoming-webhook](https://slack.com/services/new/incoming-webhook) から Webhook URL を取得し

```
# config.yml
webhook_url: https://hooks.slack.com/services/xxxx
```

と設定する。

また、特定IPからのアクセスの際に通知したくない場合には

```
# config.yml
ignore_ip_list:
  - xxx.xxx.xxx.xxx
  - yyy.yyy.yyy.yyy
```

を設定する。

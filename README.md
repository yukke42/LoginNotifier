# LoginNotifier

サーバーにSSHログインがあった際にSlackに通知する。


# Settings

```
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ sudo sh -c "echo '$PWD/bin/python $PWD/notify.py $PWD \$USER \$SSH_CLIENT' > /etc/ssh/sshrc"
$ deactivate
```


# sadb
(safe adb)Easy your adb operation when connected multiple devices

[![PyPI version](https://badge.fury.io/py/sadb.svg)](https://badge.fury.io/py/sadb)

It's painful to use adb commands if your computer has connected multiple devices, especially you type a very long command and adb shows error that there has multiple devices and you need to try it again with the device's identity argument.

`sadb` was created by solving this problem, no `-s` argument need anymore, you can also use one command to operate multiple devices in batch:
![](https://raw.githubusercontent.com/linroid/sadb/master/screenshots.png)

### Install
---

`sadb` has already uploaded to [PYPI](https://pypi.python.org/pypi/sadb)，so the simplest way is to install by pip：

```
$ pip install sadb
```

Also，you can install from source code：

```
$ git clone git@github.com:linroid/sadb.git
$ cd sadb
$ python setup.py install
```

### Usage

Use `sadb` as same as the orignal `adb` command, it will let you choose target devices when needed.


### Upgrade：

```
$ pip install sadb --upgrade
```


### License
---

Apache License 2.0 ([here](https://github.com/linroid/sadb/blob/master/LICENSE))

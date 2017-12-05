# sadb
(safe adb)在多设备时更方便地操作adb，支持批量操作。

[![PyPI version](https://badge.fury.io/py/sadb.svg)](https://badge.fury.io/py/sadb)

如果你的电脑连了多台设备，又需要直接使用adb命令时，会非常痛苦（特别是输完长长的命令后，还得回头 `adb devices` 后编辑命令重新执行）。
`sadb` 很好地解决了这个问题，不再需要你手动加 -s 参数，甚至可以一条命令对多台设备进行操作：
![](https://raw.githubusercontent.com/linroid/sadb/master/screenshots.png)

### 使用
你完全可以把 `sadb` 当成 `adb` 来使用，如果检测到有多设备时，`sadb`会自动让你选择需要操作的设备。
你也可以设置别名，来让 `sadb` 替代`adb`:

```bash
alias adb="sadb"
```

### 安装
---

`sadb` 已经上传到了 [PYPI](https://pypi.python.org/pypi/sadb)，所以最简单的安装方式就是使用 pip：

```
$ pip install sadb
```

更新：

```
$ pip install sadb --upgrade
```

当然，你也可以通过源码安装：

```
$ git clone git@github.com:linroid/sadb.git
$ cd sadb
$ python setup.py install
```


### License
---

Apache License 2.0 ([here](https://github.com/linroid/sadb/blob/master/LICENSE))

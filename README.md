[![CircleCI](https://circleci.com/gh/a1008u/PythonTraining/tree/master.svg?style=svg)](https://circleci.com/gh/a1008u/PythonTraining/tree/master)

# PythonTraining
Pythonの理解を深めるためのトレーニング用


```
# pythonのテストコード全てを実行する
coverage -m unittest

# covrageのレポートをみる
coverage report -m
```


## python lint
[autopep8 – PythonコードをPEP 8スタイルガイドに準拠するように自動的にフォーマットするツール](https://githubja.com/hhatto/autopep8)

```
# スタイルチェック
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

# コード修正
autopep8 --in-place --aggressive --aggressive　<filename>
```

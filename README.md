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
autopep8 --in-place --aggressive　<filename>
```

## アルゴリズム

- ソート
- サーチ
- リスト
- ハッシュテーブル
- スタック・キュー
- ツリー

プラスα
- ベルマン・フォード法
- ダイクストラ法
- A*アルゴリズム
- 文字列探索の力任せ法
- Boyer-Moore法
- 逆ポーランド記法
- ユークリッドの互除法

## ソート一覧表

| ソート | AVE | BEST | WORST | 安定 | 備考 |
|---|---|---|---|---|---|
| bogo | O((n+1)!) | O(n) | Unbounded | NO |  |
| **bubble** | O(n\^2) | O(n) | O(n\^2) | YES |  |
| cocktail | O(n\^2) | O(n) | O(n\^2) | YES | bubble sortの改良 |
| comb | O(n\^2/2**g) | O(n log n) | O(n\^2) | NO | bubble sortの改良 |
| **selection** | O(n\^2) | O(n\^2) | O(n\^2) | YES | bubble sortの改良 |
| gnome | O(n\^2) | O(n) | O(n\^2) | YES |  |
| **insertion** | O(n\^2) | O(n) | O(n\^2) | YES |  |
| bucket | O(n+k) | O(n+k) | O(n\^2) | YES |  |
| shell | Depends on gap sequence | O(n log n) | O(n\^2) | NO |  |
| count | O(n) | O(n) | O(n\^2) | YES |  |
| radix | O(n) | O(n) | O(n) | YES | count sortの改良 |
| **quick** | O(n log n) | O(n log n) | O(n\^2) | NO |  |
| **merge** | O(n log n) | O(n log n) | O(n log n) | YES |  |
| **heap** |  | O(n log n) | O(n log n) | O(n log n) | NO |
| timesort | O(n log n) | O(n) | O(n log n) | YES | insertion sortとmerge sortを使用 |


# まとめ
- Pythonは、動的型付けと、シンプルで一貫した構文およびセマンティクスを備えた、最新の高水準言語です。
- Pythonはマルチプラットフォームで高度にモジュール化されており、迅速な開発と大規模プログラミングの両方に適しています。
- それはかなり高速であり、高速化のためにCまたはC ++モジュールで簡単に拡張できます。
- Pythonには、永続オブジェクトストレージ、高度なハッシュテーブル、拡張可能なクラス構文、ユニバーサル比較関数などの高度な機能が組み込まれています。
- Pythonには、数値処理、画像操作、ユーザーインターフェイス、Webスクリプトなどの幅広いライブラリが含まれています。
- 動的なPythonコミュニティによってサポートされています。

Pythonの一般的なルール

|Situation          |Suggestion                                  | Example
|-------------------|--------------------------------------------|--------|
|モジュール/パッケージ名| ショート、すべて小文字、必要な場合のみアンダースコア| imp, sys|
|関数名| すべて小文字、 underscores_for_readablitiy |foo()、my_func()
|変数名| すべて小文字、アンダースコア_for_readablitiy |my_var
|クラス名| CapitalizeEachWord | MyClass|
|定数名| ALL_CAPS_WITH_UNDERSCORES | PI、TAX_RATE|
|インデント| レベルごとに4つのスペース、タブなし|	 |
|比較| my_var: my_varでない場合は、明示的にTrueまたはFalseと比較しない。| |


|Python type         |Immutable?                | Hashable? | Dictionary key?|
|--------------------|--------------------------|-----------|----------------|
|int |Yes	|Yes	|Yes|
|float	|Yes	|Yes	|Yes|
|boolean	|Yes	|Yes	|Yes|
|complex	|Yes	|Yes	|Yes|
|str	|Yes	|Yes	|Yes|
|bytes	|Yes	|Yes	|Yes|
|bytearray	|No	|No	|No|
|list	|No	|No	|No|
|tuple	|Yes	|Sometimes	|Sometimes|
|set	|No	|No	|No|
|frozenset	|Yes	|Yes	|Yes|
|dictionary	|No	|No	|No|

## Boolean
- 0, 0.0, 0+0jは全てFalseであり、それ以外の数値は全てTrueである。
- 空の文字列 "" は False であり、その他の文字列はすべて True です。
- 空のリスト [] は False、その他のリストは True です。
- 空の辞書 {} は False であり、他のどの辞書も True です。
- 空のset set() は False、他のセットは True です。
- Python の特別な値 None は常に False です。

```python
# 同じ意味になる。
if 0 < x and x < 10:
if 0 < x < 10:
```
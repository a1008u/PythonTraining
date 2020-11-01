
# Big O Notation

## 参考

- [ランダウの記号](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%B3%E3%83%80%E3%82%A6%E3%81%AE%E8%A8%98%E5%8F%B7)
- [計算量オーダーについて](https://qiita.com/asksaito/items/59e0d48408f1eab081b5)

## 説明

- 計算量は<にいくほど、大きくなる。  
O(1) <  O(log(n)) < O(n) < O(n * log(n)) < O(n**2)

### O(1)
- 定数時間
- 処理時間がデータ量に依存しない（必ず一発で取得できる）。
``` python
def func1(numbers):
    return numbers[0]
```

### O(log(n))
- 対数時間
- 処理をひとつ行うたびに処理対象を何割か減らせるようなアルゴリズム。  
  データ量が増えても計算時間がほとんど増えない。  
  多くの場合、これ以上の改善はする必要はない。
``` python
def func2(numbers):
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)
```

### O(n)
- 線形時間
- データ量の分だけ時間がかかる。  
  forループ１回分。  
  N回もしくはNに比例する回数以内のループで処理が終わる場合。
``` python
def func3(numbers):
    for num in numbers:
        print(num)
```

### O(n * log(n))
- 準線形、線形対数時間
- ちょっと重いO(N)程度。  
  マージソートのように二分木でデータを分割し、  
  かつそれらをリニアサーチするようなアルゴリズムの計算量。  
  二分木のオーダー(logN)×リニアサーチのオーダー(N)をかけあわせてNlogNになる。
``` python
def func4(numbers):
    # O(n)
    for num in range(int(numbers)):
        print(i, end=' ')
    print()

    # O(log(n))
    if n <= 1:
        return
    eles:
        print(n)
        func4(n/2)
```

### O(n**2)
- 二乗時間
- 要素からすべての組み合わせのペアについて調べるようなアルゴリズム。  
  工夫しないソート処理など。二重のforループ。  
  これ以上は処理が遅すぎて使いにくい。
``` python
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()
```

# sort

## Stable SortとUnstable Sort

同一の値に対して、ソート後も順序が保証されるかされないかの違いです。
- Stable Sort : 順序が保証される。
- Unstable Sort : 順序が保証されない。

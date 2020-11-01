import copy

def mk_list():
  """
    事前にリストを宣言したり、サイズを修正したりする必要がないことに注意してください。
  """
  print([1,2,3])
  print([2, "2", [1, 2, 3]])

  ## インデックス「-1」を出力する = 末尾から数える
  print([1,2,3][-1])

  print([1,2,3,4,5][0:2])
  print([1,2,3,4,5][-2:-1])
  print([1,2,3,4,5][:3])
  print([1,2,3,4,5][2:])

  # indexを省略すると、元のリスト最初から最後までの新しいリストを作る
  test = [1,2,3,4,5]
  test2 = test[:]
  test2[1] = "test"
  print(test, test2)

def list_add():
  x = [1,2,3,4]

  # add
  x[len(x):] = [5,5,5]
  print(x)

  # add
  x[:0] = [-1,0]  
  print(x)

  # delete
  x[1:-1] = []
  print(x)

  xx = [1,2,3,4]
  xx.append(5)
  xx.append("four")
  print(xx)

  x1 = [1,2,3,4]
  x2 = [5,6]
  x1.append(x2)
  print(x1)

  ## expandを使うことで、追加要素のlistを分解して、追加する
  x3 = [1,2,3,4]
  x3.extend(x2)
  print(x3)

def list_isert():
  x = [1, 2, 3]
  x.insert(2, "hello")
  print(x)
  x.insert(0, "start")
  print(x)
  x.insert(-1, "hello2")
  print(x)

def list_del():
  x = [1, 2, 3, 4, 3, 5]
  x.remove(3)
  print(x)
  x.remove(3)
  print(x)
  # error
  # x.remove(3)

def list_sort():
  x = [3, 8, 4, 0, 2, 1]
  x.sort()
  print(x)

  y = ["Life", "Is", "Enchanting"]
  y.sort()
  print(y)

  z = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
  z.sort()
  print(z)

  # sortの指定なし
  word_list = ['Python', 'is', 'better', 'than', 'C']
  word_list.sort()
  print(word_list)

  # カスタムsort
  word_list.sort(key=compare_num_of_chars)
  print(word_list)

  x = (4, 3, 1, 2)
  y = sorted(x)
  print(x, y)

def compare_num_of_chars(string1):
  """
    カスタムsort用
  """
  return len(string1)

def list_operations():
  # inを使った判定処理
  print(3 in [1, 3, 4, 5])
  print(3 not in [1, 3, 4, 5])
  print(3 in ["one", "two", "three"])
  print(3 not in ["one", "two", "three"])

  print([1, 2, 3] + [4, 5])
  print([None] * 4)
  print([3, 1] * 2)

  print(min([3, 7, 0, -2, 11]))
  # print(max([4, "Hello", [1, 2]])) エラー

  print([1, 3, "five", 7, -2].index(3))
  # print([1, 3, "five", 7, -2].index(5)) エラー
  print([1, 3, "five", 7, -2].index(7))

  # list内の指定された要素を数える
  print([1, 2, 2, 3, 5, 2, 5].count(2))
  print([1, 2, 2, 3, 5, 2, 5].count(7))

def list_deepcopy():
  m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
  print(m[0], m[0][1], m[2], m[2][2])

  nested = [0]
  original = [nested, 1]
  print(nested, original)

  nested[0] = 'zero'
  print(nested, original)

  original[0][0] = 0
  print(nested, original)

  # 参照先が別の値を見ると、それを見ている参照元は参照先の新しい値を見ることができない
  # 参照することができなくなる
  nested = [2]
  print(nested, original)

  original = [[0], 1]
  # 浅いコピー
  shallow = original[:]
  print(shallow, original)
  
  # 深いコピー
  deep = copy.deepcopy(original)
  print(deep, shallow, original)

  # shallowのみ値が変更
  shallow[1] = 2
  print(deep, shallow, original)

  # listのため、shallowとoriginalが変更
  shallow[0][0] = 'zero'
  print(deep, shallow, original)

  # deepcopyをしているため、deepは変更しない
  # オリジナルから独立している
  deep[0][0] = 5
  print(deep, shallow, original)

def mk_tuple():
  """
    javaでいうset
    タプルは不変である
  """
  print(('a', 'b', 'c'))
  print(('a', 'b', 'c')[1])
  print(('a', 'b', 'c')[1:])
  print(1 in ('a', 'b', 'c'))
  print(1 not in ('a', 'b', 'c'))

  a1 = ('a', 'b', 'c')
  b1 = ('a', 'b', 'c')
  print(a1 + b1)
  print(2 * a1)

  x = 3
  y = 4
  # +の演算
  print((x + y))
  # タプル
  print((x + y,))

def tuple_sampel():
  x = (1, 2, 3, 4)
  a, b, * c = x 
  print(a,b,c)

  a,* b, c = x 
  print(a,b,c)

  * a, b, c = x 
  print(a,b,c)

  a, b, c, d, *e = x
  print(a, b, c, d, e)

def convert_list_tuples():
  # tuple => list
  print(list((1, 2, 3, 4)))
  # list => tuple
  print(tuple([1, 2, 3, 4]))
  # listは文字列を文字に分解する
  print(list("Hello"))

def mk_set():
  x = set([1, 2, 3, 1, 3, 5])  
  print(x)

  x.add(6)       
  print(x)    

  x.remove(5)   
  print(x)

  print(1 in x)
  print(4 in x)

  y = set([1, 7, 8, 9])
  print(x | y)
  print(x & y)
  print(x ^ y)

def mk_frozensets():
  """
    frozensetを利用することで、setのオブジェクトに値を追加することができなくなる。
  """
  x = set([1, 2, 3, 1, 3, 5])
  z = frozenset(x)
  print(z, x)

  x.add(z)
  print(z, x)

if __name__ == '__main__':
  mk_list()
  list_add()
  list_isert()
  list_del()
  list_sort()
  list_operations()
  list_deepcopy()

  mk_tuple()
  tuple_sampel()
  convert_list_tuples()

  mk_set()
  mk_frozensets()
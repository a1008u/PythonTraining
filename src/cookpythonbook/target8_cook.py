import logging

def t1():
  print("t1")
def t2():
  print("t2")
def t3():
  print("t3")

def mk_if():
  x =0
  if x < 5:
      pass
  else:
      x = 5
  print("done")

  # pythonにはcaseがないので、case相当の書き方
  func_dict = {'a' : t1,
               'b' : t2,
               'c' : t3 }
  x = 'a'
  func_dict[x]()    

def mk_for():
  """
  forループは反復可能なオブジェクト、
  つまり一連の値を生成できるオブジェクトから返された値を反復処理します。
  """
  for n in [1.0, 2.0, 3.0]:
    print(1 / n)

  # indexを取得する場合はrange
  x = [1, 3, -7, 4, 9, -5, 4]
  for i in range(len(x)):
    if x[i] < 0:
        print("Found a negative number at index ", i)
  
  logging.info(list(range(3, 7)))
  logging.info(list(range(2, 10)))
  logging.info(list(range(5, 3)))
  logging.info(list(range(0, 10, 2)))
  logging.info(list(range(5, 0, -1)))

  result = 0
  for t in [(1, 2), (3, 7), (9, 5)]:
    result = result + (t[0] * t[1])
  logging.info(f"result is {result}")

  # unpack
  result2 = 0
  for x, y in [(1, 2), (3, 7), (9, 5)]:
      result2 = result2 + (x * y)
  logging.info(f"result2 is {result2}")

  # enumerate関数を利用することで、indexと値を取得できる
  x = [1, 3, -7, 4, 9, -5, 4]
  for i, n in enumerate(x):
      if n < 0:
          print("Found a negative number at index ", i)

  # zipをもちいて、2つのlistをlist + tupleの形にしてくれる
  x = [1, 2, 3, 4]
  y = ['a', 'b', 'c']
  z = zip(x, y)
  logging.info(f"z is {z}")
  logging.info(f"list(z) is {list(z)}")

def mk_list_and_dict():
  x = [1, 2, 3, 4]
  x_squared = []
  for item in x:
    x_squared.append(item * item)
  logging.info(x_squared)

  # ショートカット
  # new_list = [expression1 for variable in old_list if expression2]
  x_squared = [item * item for item in x]
  logging.info(x_squared)

  # for -> if -> 演算 -> list
  x_squared = [item * item for item in x if item > 2]
  logging.info(x_squared)

  # for -> 演算 -> dict
  x_squared_dict = {item: item * item for item in x}
  logging.info(x_squared_dict)

  # ジェネレータ式
  # リスト内包とにているが、 ()を利用しているまた、戻り値がgenerator
  x = [1, 2, 3, 4]
  x_squared = (item * item for item in x)
  logging.info(x_squared)
  for square in x_squared:
    logging.info(square,)

def ck_statements_block_indentation():

  # セミコロン（;）を利用すると、複数のブロックも一行で記載できる。
  x = 1; y = 0; z = 0
  if x > 0: y = 1; z = 10
  else: y = -1
  print(x, y, z)

  # and演算子は、
  # Falseなら、最初の false オブジェクト (式が評価される) 
  # Trueなら、最後のオブジェクトを返します。
  print([2] and [3, 4])
  print([] and 5)

  # or 演算子は、最初の真のオブジェクトか最後のオブジェクトを返します。
  print([2] or [3, 4])
  print([] or 5)
  print([] or [])

  x = [0]
  y = [x, 1]
  logging.info(x is y[0])
  x = [0] 
  logging.info(x is y[0])

  # 値を確認する
  logging.info(x == y[0])

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)


  mk_if()
  logging.warning("--------------------------------------")

  mk_for()
  logging.warning("--------------------------------------")

  mk_list_and_dict()
  logging.warning("--------------------------------------")

  ck_statements_block_indentation()
  logging.warning("--------------------------------------")
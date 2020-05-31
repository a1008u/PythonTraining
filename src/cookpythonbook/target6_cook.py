
def ck_join_split():
  print(" ".join(["join", "puts", "spaces", "between", "elements"]))
  print("::".join(["Separated", "with", "colons"]))
  print("".join(["Separated", "by", "nothing"]))

  # デフォルトでは、split は空白一文字だけでなく、任意の空白に対しても分割します。
  x = "You\t\t can have tabs\t\n \t and newlines \n\n " \
               "mixed in"
  print(x.split())

  x = "Mississippi"
  print(x.split("ss"))

  # splitの第二引数は「オプションの第二引数で、結果を生成する際にsplitが実行すべき分割数を指定します。」
  x = 'a b c d'
  print(x.split(' ', 1))
  print(x.split(' ', 2))
  print(x.split(' ', 9))

def ck_convert():
  print(float('123.456'))
  # print(float('xxyy'))
  print(int('3333'))
  # print(int('123.456') )

  # int(対象の数字, 変換用の進数設定) => 10000を8進数へ
  print(int('10000', 8))
  print(int('101', 2))
  print(int('ff', 16))

def ck_extra():
  # stripは元の文字列と同じ新しい文字列を返しますが、文字列の先頭と末尾の空白が取り除かれています。
  x = "  Hello,    World\t\t "
  print(x.strip())
  print(x.lstrip())
  print(x.rstrip())

  # 文字を指定することで、対象の文字は削除できる
  x = "www.python.org"
  print(x.strip("w"))
  print(x.strip("gor"))
  print(x.strip(".gorw"))

def ck_search():
  x = "Mississippi"
  print(x.find("ss"))
  print(x.find("zz"))

  # 第二引数はstartを示す(3文字以降)
  # 第３引数はendを示す(0-3文字の間)
  x = "Mississippi"
  print(x.find("ss", 3))
  print(x.find("ss", 0, 3))

  # 検索をstringの終わりから開始し、string内の最後のsubstringの最初の文字の位置を返します。
  x = "Mississippi"
  print(x.rfind("ss"))

  x = "Mississippi"
  print(x.count("ss"))

  x = "Mississippi"
  print(x.startswith("Miss"))
  print(x.endswith("pi"))
  print(x.endswith("p"))
  # 引数を複数指定するにはタプルを利用し、どちらかが存在したらtrueとなる
  print( x.endswith(("i", "u")))

def ck_modifying():
  x = "Mississippi"
  print(x.replace("ss", "+++"))

  # maketrans を使って 2 つの文字列の引数から翻訳テーブルを作ります。
  # 2つの引数はそれぞれ同じ文字数を含んでいなければならず、
  # 最初の引数のn番目の文字を調べると2番目の引数のn番目の文字が返ってくるようなテーブルが作られます。
  x = "~x ^ (y % z)"
  table = x.maketrans("~^()", "!&[]")
  print(x.translate(table), table)

  ## 新しい文字列オブジェクトの作成と破棄が発生し、比較的コストがかかるので、やりすぎないようにしましょう。
  text = "Hello, World"
  wordList = list(text)
  print(wordList)
  wordList[6:] = []
  wordList.reverse()
  text = "".join(wordList)
  print(text)    

def ck_converting():
    # repr を使用してリスト x を文字列表現に変換
    print(repr([1, 2, 3]))
    x = [1]
    x.append(2)
    x.append([3, 4])
    print('the list x is ' + repr(x))

def ck_format():
  print("{0} is the {1} of {2}".format("Ambrosia", "food", "the gods"))
  print("{{Ambrosia}} is the {0} of {1}".format("food", "the gods"))
  print("{food} is the food of {user}".format(food="Ambrosia",user="the gods"))
  print("{0} is the food of {user[1]}".format("Ambrosia",user=["men", "the gods", "others"]))

  print("{0:10} is the food of gods".format("Ambrosia"))
  print("{0:{1}} is the food of gods".format("Ambrosia", 10))
  print("{food:{width}} is the food of gods".format(food="Ambrosia", width=10))
  print("{0:>10} is the food of gods".format("Ambrosia"))
  print("{0:&>10} is the food of gods".format("Ambrosia"))

  print("%s is the %s of %s" % ("Ambrosia", "food", "the gods"))
  print("%s is the %s of %s" % ("Nectar", "drink", "gods"))
  print("%s is the %s of the %s" % ("Brussels Sprouts", "food","foolish"))

  x = [1, 2, "three"]
  print("The %s contains: %s" % ("list", x))

  print("Pi is <%-6.2f>" % 3.14159)

  num_dict = {'e': 2.718, 'pi': 3.14159}
  print("%(pi).2f - %(pi).4f - %(e).2f" % num_dict)

def ck_string_interpolation():
  """
   文字列補間
  """
  value = 42
  message = f"The answer is {value}"
  print(message)

  pi = 3.1415
  print(f"pi is {pi:{10}.{2}}")

def ck_bytes():
  """
  覚えておくべき重要なことは、バイトオブジェクトは文字列のように見えるかもしれませんが、
  文字列のように正確に使用したり、文字列と組み合わせたりすることはできないということです。
  """
  unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
  print(unicode_a_with_acute) 

  xb = unicode_a_with_acute.encode()
  print(xb, " -> ", xb.decode())

if __name__ == '__main__':
  ck_join_split()
  ck_convert()
  ck_extra()
  ck_search()
  ck_modifying()
  ck_converting()
  ck_format()
  ck_string_interpolation()
  ck_bytes()
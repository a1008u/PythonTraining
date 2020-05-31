
import logging



def mk_dictonary():
  x = []
  y = {}
  
  print("this is the list => ", x)
  print("this is the dictonary => ", y)

  y[0]="hello"
  y[1]="world"
  y["hello"]="WORLD"
  print(y)

  english_to_french = {}
  english_to_french['red'] = 'rouge' 
  english_to_french['blue'] = 'bleu'
  english_to_french['green'] = 'vert'
  print("red is", english_to_french['red'])

  # listだと存在しないINDEXに値を格納するとエラーとなる。（appendなどを利用）
  # x.append("test")
  # x[1] = "testlist"

def ck_dictonary_ope():
  english_to_french = {'red': 'rouge', 'blue': 'bleu', 'green': 'vert'}
  logging.info(english_to_french)
  logging.info(len(english_to_french))
  logging.info(f"english_to_french(key) is {list(english_to_french.keys())}")
  logging.info(f"english_to_french(values) is {list(english_to_french.values())}")

  # dictonaryをlistに変換すると、list -> tupleの構造で保持している
  logging.info(f"english_to_french is {list(english_to_french.items())}")

  del english_to_french['green']
  logging.info(f"english_to_french is {list(english_to_french.items())}")

  # dictならinを利用することもできる
  print('red' in english_to_french, 'orange' in english_to_french)

  # dictに値が存在しない場合の処理に空でなく、デフォルトの文字をしていすることもできる
  print(english_to_french.get('blue', 'No translation'))
  print(english_to_french.get('chartreuse', 'No translation'))

  # setdefault(key, default-value)
  print(english_to_french.setdefault('chartreuse', 'No translation'))
  logging.info(f"english_to_french is {list(english_to_french.items())}")

  x = {0: 'zero', 1: 'one'}

  # shallow copy
  y = x.copy()
  print(f"x is {x}", " ", f"y is {y}")

  z = {1: 'One', 2: 'Two'}
  x = {0: 'zero', 1: 'one'}
  x.update(z)
  print(f"x is {x}", " ",f"z is {z}")

def ck_wordcounting():
  sample_string = "To be or not to be"
  occurrences = {}
  for word in sample_string.split():
    occurrences[word] = occurrences.get(word, 0) + 1

  for word in occurrences:
    print("The word", word, "occurs", occurrences[word],"times in the string")

def ck_sparse_matrices():
  matrix = [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
  logging.info(matrix)

  # {(rownum, colnum): value}
  matrix = {(0, 0): 3, 
            (0, 2): -2, 
            (0, 3): 11, 
            (1, 1): 9, 
            (2, 1): 7, 
            (3, 3): -5}
  logging.info(matrix)


if __name__ == '__main__':

  logging.basicConfig(level=logging.DEBUG)
  
  mk_dictonary()
  logging.warning("--------------------------------------")

  ck_dictonary_ope()
  logging.warning("--------------------------------------")

  ck_wordcounting()
  logging.warning("--------------------------------------")

  ck_sparse_matrices()
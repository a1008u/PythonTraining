from src.cookpythonbook import target3_cook

def mainExec():
  n = 9
  r = 1
  while n > 0:
      r = r * n 
      n = n - 1 
  print(n, r)
  
if __name__ == '__main__':
  mainExec()
  target3_cook.Variables()
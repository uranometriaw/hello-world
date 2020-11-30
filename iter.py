string = 'Hello! World!'
s = iter(string)
while True:
  try:
      print(next(s))
  except:
      break
# 这是迭代器的内容吗？

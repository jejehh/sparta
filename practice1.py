
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

def count_list(a_list):
  result = {}
  for element in fruits:
    if element in result:
      result[element] += 1
    else:
      result[element] = 1
  return result

print(count_list(a))

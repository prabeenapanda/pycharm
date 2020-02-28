#Write a python program to find first non repeating character in a string
def character(str1):
  order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1
      order.append(c)
  print(order)
  print(ctr)
  for c in order:
    if ctr[c] == 1:
      return c
  return None

print(character('abcdef'))
print(character('abcabcdef'))
print(character('aabbcc'))

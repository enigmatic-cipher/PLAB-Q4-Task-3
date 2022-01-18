"""
Given a string as input. Create a new string with all the lowercase characters removed.
Input-> "TableTennis"
Output-> "TT"
"""

st = "TableTennis"
ln = len(st)
strn = ""
for i in range(0,ln):
  ch = st[i]
  if (ch>="a" and ch<="z"):
    pass
  else:
    strn = strn + ch
print(strn)

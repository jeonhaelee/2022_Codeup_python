

def f(n, star):
  if len(star) == n:
    return 0
  else:
    star += "*"
    print(star)
    f(n, star)


star = ""
n = int(input())
f(n, star)
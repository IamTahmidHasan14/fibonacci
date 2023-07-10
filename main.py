def fibo(n):
  a = 0
  b = 1
  print(a, end=",")
  print(b, end=",")
  for i in range(n - 2):
    c = a + b
    print(c, end=",")
    a = b
    b = c
  print()


print("Fibonacci of 5 is:")
fibo(5)
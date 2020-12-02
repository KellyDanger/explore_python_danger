msg = "Hello World"
print(msg)

print ("hello world")

def hello_function(name):
  print ("hello", name)
  return

hello_function("elliot")

def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    print ("fizzbuzz")
  elif num % 3 == 0:
    print("fizz")
  elif num % 5 == 0:
    print("buzz")
  else:
    print(num)


fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(7)
fizz_buzz(9)

x = int('4')
y=[]


print(x)
print(type(x))
print(type(y))

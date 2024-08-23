x = "Ajit"

def fun():
  x = "Kumar"
  print("Python is good " + x)

fun()

print("Python is good " + x)

def sorrow():
  global x
  x = "welldone"

sorrow()

print("Python is good " + x)

x = "india"

def rest():
  global x
  x = "fantastic"

rest()

print("Python is good " + x)
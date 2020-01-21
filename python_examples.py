def demo(p):
 	x,y = p
p[0] = ‘c’
return(x,y)


demo((1,2))
demo([1,2])


def demo2(L):
    L[0] = ‘c’
    return(L[0],L[1])

myL = [1,2,3]
demo2(myL])
myL


def demo3(L):
    L =[‘a’,’b’,’c’]
    return(L[0],L[1])

demo3(myL)
myL


#global, local
def f():
 	print(s)
 	s = "Me too."
 	print(s)


s = "I hate spam."
f()
print(s)


def f():
    global s
    print(s)
    s = "That's clear."
    print(s)


s = "Python is great!"
f()
print(s)



y = 5 
z = 1
x = 3
def f(y):
   z = 4
   def g(a):
      z = 2
      return a+x+z
   return y+z+g(10)
print ('result',f(4))
print('z:',z)
print('x:',x)

y = 5 
z = 1
x = 3
def f(y):
   z = 4
   def g(a):
      global z
      print('z in g:',z)
      z = 2
      return a+x+z
   return y+z+g(10)
print ('result:',f(4))
print('z:',z)
print('x:',x)


y = 5 
z = 1
x = 3
def f(y):
   z = 4
   def g(a):
      nonlocal z
      print('z in g:',z)
      z = 2
      return a+x+z
   return y+z+g(10)
print ('result:',f(4))
print('z:',z)
print('x:',x)

class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   # pass
   def a(self):
       return 'boo'

class D(C, A, B):
   pass

d = D()
print(d.a())
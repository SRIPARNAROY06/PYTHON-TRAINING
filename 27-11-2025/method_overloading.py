# class MathOps:
#     def add(self,a,b=0,c=0):
#         return a+b+c
#
# n=MathOps()
# print(n.add(5))
# print(n.add(5,10))
# print(n.add(5,10,20))
#

class MathOps:
    def add(self, *args):
        return sum(args)

m=MathOps()
print(m.add(3,4))
print(m.add(3))
print(m.add(3,4,5,6))
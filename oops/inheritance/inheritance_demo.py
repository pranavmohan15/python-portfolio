#1.single level inheritance
#single parent-->single child

# class parent():
#     def demo(self):
#         print('demo A')
# class child(parent):
#     def test(self):
#         print('test')
# obj=child()


# 2.multilevel
# parent-->child-->grandchild

class parent:
    def demo(self):
        print('demo A')
class child(parent):
    def test(self):
        print('test')
class grandchild(child):
    def t(self):
        print('hi')
obj=grandchild()

# 3.multiple inheritance
class parent1:
    def demo(self):
        print('demo A')
class parent2:
    def test(self):
        print('test')
class child(parent1,parent2):
    def t(self):
        print('hi')
obj=child()

# 4.hierarchical inheritance
class parent1:
    def demo(self):
        print('demo A')
class child1(parent):
    def test(self):
        print('test')
class child2(parent):
    def t(self):
        print('hi')
obj1=child1()
obj2=child2()
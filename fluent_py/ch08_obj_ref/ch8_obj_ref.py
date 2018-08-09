'''
garbage collection, the del command, and how
to use weak references to “remember” objects without keeping them alive.
reference variables: label attached to objects

下面可以证明赋值是先evluate右边再绑定到左边(Gizmo实例创建成功但是y并没有赋值成功)
To  understand  an  assignment  in  Python,  always  read  the  right-
hand side first: that’s where the object is created or retrieved. Af‐
ter that, the variable on the left is bound to the object, like a label
stuck to it. Just forget about the boxes.
值相等 == 就为True(__eq__实现)
is比较identity
tuple里面的元素是mutable
tuple += 会产生一个新的


 The problem is that each default value is eval‐
uated when the function is defined—i.e., usually when the module is loaded—and the
default values become attributes of the function object. So if a default value is a mutable
object, and you change it, the change will affect every future call of the function.
弱引用 An element will be discarded when no strong
reference to it exists any more.
 If you need to build a class that is aware of every one of
its instances, a good solution is to create a class attribute with a WeakSet to hold the
references to the instances. Otherwise, if a regular set was used, the instances would
never be garbage collected, because the class itself would have strong references to them,
and classes live as long as the Python process unless you deliberately delete them.



'''
#eg1
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
y = Gizmo() * 10 #报错但是实例已经生成 


#eg2
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)      # 
l1.append(100)     # 
l1[1].remove(55)   # 
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]  # 
l2[2] += (10, 11)  # 
print('l1:', l1)
print('l2:', l2)

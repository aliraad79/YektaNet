class A:
    def __init__(self, id):
        self.id = id

class B(A):
    def __init__(self, id , name):
        super().__init__(id)
        self.name = name


a = A(1)
b = B(2,'ali')

print(a.id, b.id,b.name)
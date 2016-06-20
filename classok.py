class Parent(object):
    static = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    A = [Parent('Bela'+str(i), i*i) for i in range(5)]
    for i in A:
        print i.name, i.age

# 1 Iterator to return elements in a list:

class ReverseIterator:

    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


lst = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(lst)

for elem in reverse_iter:
    print(elem)

# 2 An iterator that rotates all paired numbers in the range from 0 to N:

class EvenIterator:

    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

N = 10
even_iter = EvenIterator(N)

for num in even_iter:
    print(num)

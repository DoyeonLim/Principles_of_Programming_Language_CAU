class sort_gen():
    def __init__(self, data):
        self.data = data
        self.remain = []
        self.tail = []
        self.head = []
        self.target = []
        self.result = []
    def sort(self, data):
        if len(self.data) == 0:
            if not len(self.head) == 0:
                self.data = self.remain[-1]
                del self.remain[-1]
                self.result = self.head[-1]
                del self.head[-1]
                return True
            elif len(self.head) == 0:
                self.data = self.remain[-1]
                del self.remain[-1]
                return self.sort(self.data)
        elif not len(self.data) == 0:
            self.target = self.data[0]
            self.tail = self.data[1:]
            self.head.append(self.target)
        self.less = [v for v in self.tail if v < self.target]
        self.data = self.less
        self.greater = [v for v in self.tail if v >= self.target]
        self.remain.append(self.greater)
        return self.sort(self.data)
    def __next__(self):
        if self.sort(self.data) == True:
            return self.result
        raise StopIteration
    def __iter__(self):
        return self

data = [3, 1, -5, 7, -4, 2, 6, 200, 9, -2, 4, 3, 0, -2] + [100] * 100000

for _, val in zip(range(20), sort_gen(data)):
    print(val, end=" ")

sum = 0

for val in sort_gen(data):
    sum += val * val
    if sum > 50:
        print('\nSum =', sum)
        break

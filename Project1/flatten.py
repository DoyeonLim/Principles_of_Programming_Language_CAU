class new_flatten:
    def __init__(self, data):
        self.data = data
        self.space = []
        self.result = []
    def flatten(self, data):
        if isinstance(self.data, int):
            self.result = self.data
            self.data = self.space[-1]
            del self.space[-1]
            return True
        elif isinstance(self.data, list):
            if not len(self.data) == 1:
                self.space.append(self.data[1:])
            self.data = self.data[0]
            return self.flatten(self.data)
    def __next__(self):
        if self.flatten(self.data) == True:
            return self.result
        raise StopIteration
    def __iter__(self):
        return self

data = [1, [2, [[[4]]], [0, 5], [], 3], [4], 2, 7]
sum = 0

for e in new_flatten(data):
    print(e)
    sum += e
    if sum > 10:
        break
print('Result:', sum)




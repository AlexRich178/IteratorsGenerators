nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

my_list = [1, 2, 3, 't']


class FlatIterator:
    def __init__(self, x_list):
        self.list = x_list

    def __iter__(self):
        self.one_list = [*self.list[0], *self.list[1], *self.list[2]]
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.one_list):
            raise StopIteration
        return self.one_list[self.cursor]


my_range = FlatIterator(nested_list)
for i in my_range:
    print(i)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def flat_generator(x_list):
    return (next_value for next_list in x_list for next_value in next_list)


for item in flat_generator(nested_list):
    print(item)

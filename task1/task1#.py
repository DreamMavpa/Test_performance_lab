import argparse

class My_Array:
    def __init__(self, n):
        self.n: int = n
        self.num: int = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        return self.next()

    def next(self) -> int:
        if self.num < self.n:
            pointer, self.num = self.num, self.num + 1
        else:
            pointer, self.num = self.num, 1
        
        return pointer


def answer(n, m):
    if m > n:
        m = m % n
        if m == 0:
            m = n

    my_arr = My_Array(n)
    pointer = next(my_arr)
    path = [pointer]

    for _ in range(m-1):
        pointer = next(my_arr)
    
    if pointer == 1:
        return "".join([str(x) for x in path])
    path.append(pointer)

    while pointer != 1:
        for _ in range(m-1):
            pointer = next(my_arr)
        if pointer != 1:
            path.append(pointer)

    return "".join([str(x) for x in path])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)
    args = parser.parse_args()
    n, m = args.n, args.m

    print(answer(n, m))
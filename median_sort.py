import sys

def parse_input():
    return [int(x) for x in input().split()]


def query(i, j, k):
    print(f"{i} {j} {k}")
    sys.stdout.flush()
    return int(input())


def insert(lst, nxt):
    if not lst:
        return [nxt]
    left = lst[0]
    middle_idx = len(lst)//2
    middle = lst[middle_idx]
    median = query(left, middle, nxt)
    if median == left:
        return [nxt] + lst
    if median == middle:
        if len(lst) == 2:
            return lst + [nxt]
        if len(lst) == 3:
            return [left] + insert(lst[1:], nxt)
        if len(lst) == 4:
            return lst[:middle_idx] + insert(lst[middle_idx:], nxt)
        return lst[:middle_idx+1] + insert(lst[middle_idx+1:], nxt)
    else:
        if len(lst) == 2:
            return [left, nxt, middle]
        if len(lst) == 3:
            return [left, nxt] + lst[middle_idx:]
        if middle_idx == 2:
            return insert(lst[:middle_idx], nxt) + lst[middle_idx:]
        return [left] + insert(lst[1:middle_idx], nxt) + lst[middle_idx:]


def build_lst(N, Q):
    lst = [1, 2]
    while len(lst) < N:
        nxt = len(lst)+1
        lst = insert(lst, nxt)
    return lst


def main():
    T, N, Q = parse_input()
    for _ in range(T):
        print(" ".join(map(str, build_lst(N, Q))))
        sys.stdout.flush()
        result = int(input())


if __name__ == "__main__":
    main()

def read_test_cases():
    T = int(input())
    for _ in range(T):
        input()
        yield [int(x) for x in input().split()]


def min_idx(lst):
    idx = -1
    val = None
    for i, v in enumerate(lst):
        if val is None or v < val:
            val = v
            idx = i
    return idx


def reverse_sort_cost(lst):
    cost = 0
    for i in range(len(lst)-1):
        j = i + min_idx(lst[i:])
        cost += j - i + 1
        lst = lst[:i] + lst[i:j+1][::-1] + lst[j+1:]
    return cost


def main():
    for i, test_case in enumerate(read_test_cases()):
        cost = reverse_sort_cost(test_case)
        print(f"Case #{i+1}: {cost}")


if __name__ == "__main__":
    main()

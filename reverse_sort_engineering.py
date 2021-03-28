def parse_input():
    T = int(input())
    for _ in range(T):
        yield [int(x) for x in input().split()]

def split_score(C, N):
    operations = [1]*(N-1)
    excess = C - (N - 1)
    for i in range(N-1):
        allocated = min(N-i-1, excess)
        operations[i] += allocated
        excess -= allocated
    return operations


def construct_list(N, C):

    if not N-1 <= C < (N*(N+1))//2:
        return "IMPOSSIBLE"

    operations = split_score(C, N)

    lst = list(range(1, N+1))
    for i, rev in enumerate(operations[::-1]):
        start = N - 2 - i
        end = start + rev
        lst = lst[:start] + lst[start:end][::-1] + lst[end:]

    return " ".join(map(str, lst))


def main():
    for i, case in enumerate(parse_input()):
        print(f"Case #{i+1}: {construct_list(*case)}")


if __name__ == "__main__":
    main()

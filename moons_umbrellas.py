def parse_input():
    T = int(input())
    for _ in range(T):
        case = input().split()
        X = int(case[0])
        Y = int(case[1])
        yield X, Y, case[2]


def min_cost(X, Y, string):
    cost = 0
    pointer = 0
    string = string.strip("?")
    start = None
    for i, char in enumerate(string):
        if char == "?":
            if start is None:
                start = string[i-1]
        elif start is not None:
            end = char
            if start != end:
                cost += X if start == "C" else Y
            start = None
        if i > 0:
            if string[i-1:i+1] == "CJ":
                cost += X
            elif string[i-1:i+1] == "JC":
                cost += Y
    return cost


def main():
    for i, test_case in enumerate(parse_input()):
        print(f"Case #{i+1}: {min_cost(*test_case)}")


if __name__ == "__main__":
    main()

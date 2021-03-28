import numpy as np
from collections import defaultdict

def parse_input():
    T = int(input())
    P = int(input())
    for _ in range(T):
        results = []
        for _ in range(100):
            results.append([int(x) for x in input()])
        yield np.array(results)


def guess_cheater(results):
    level = 600
    candidates = np.arange(results.shape[0])[results.sum(axis=1) > level]
    mean_corrs = (np.corrcoef(results[candidates]).sum(axis=1)-1)/len(candidates)
    min_corr = None
    guess = None
    for candidate, mean_corr in zip(candidates, mean_corrs):
        if min_corr is None or mean_corr < min_corr:
            guess = candidate
            min_corr = mean_corr
    return guess+1


def main():
    for i, case in enumerate(parse_input()):
        print(f"Case #{i+1}: {guess_cheater(case)}")


if __name__ == "__main__":
    main()

import random


def next_fit(weights):
    bins = [0]
    for w in weights:
        if bins[-1] + w <= 1:
            bins[-1] += w
        else:
            bins.append(w)
    return bins


def first_fit_decreasing(weights):
    weights = sorted(weights, reverse=True)
    bins = []
    for w in weights:
        for i, b in enumerate(bins):
            if b + w <= 1:
                bins[i] += w
                break
        else:
            bins.append(w)
    return bins


def best_fit_decreasing(weights):
    weights = sorted(weights, reverse=True)
    bins = []
    for w in weights:
        idx = None
        diff = 1
        for i, b in enumerate(bins):
            if b + w <= 1:
                if diff > 1 - (b + w):
                    diff = 1 - (b + w)
                    idx = i
        if idx:
            bins[idx] += w
        else:
            bins.append(w)
    return bins


if __name__ == '__main__':
    weights = [random.random() for _ in range(10)]
    print(weights)
    print(next_fit(weights))
    print(best_fit_decreasing(weights))
    print(first_fit_decreasing(weights))

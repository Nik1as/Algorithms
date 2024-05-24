import random


class Roulett:

    def __init__(self, prob):
        self.prob = prob

        self.A = [0] * len(self.prob)
        self.A[0] = self.prob[0]
        for i in range(len(self.prob)):
            self.A[i] = self.A[i - 1] + self.prob[i]

    def generate(self):
        x = random.random()

        start = 0
        end = len(self.A) - 1
        result = -1
        while start <= end:
            mid = (start + end) // 2
            if self.A[mid] <= x:
                start = mid + 1
            else:
                result = mid
                end = mid - 1
        return result


if __name__ == '__main__':
    prob = [0.4, 0.2, 0.15, 0.15, 0.1]
    res = [0] * len(prob)
    n = 1_000_000
    roulett = Roulett(prob)

    for _ in range(n):
        x = roulett.generate()
        res[x] += 1
    print(list(map(lambda x: x / n, res)))

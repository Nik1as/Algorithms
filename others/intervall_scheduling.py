def intervall_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    curr_end = 0
    result = []
    for start, end in jobs:
        if start >= curr_end:
            curr_end = end
            result.append((start, end))
    return result


if __name__ == '__main__':
    jobs = [(0, 1), (2, 5), (1, 10), (4, 7), (1, 3), (8, 9), (6, 8)]
    print(intervall_scheduling(jobs))

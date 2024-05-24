def weighted_interval_scheduling(jobs):
    max_end = max(j[1] for j in jobs)
    opt = [0 for _ in range(max_end + 1)]
    for t in range(max_end + 1):
        executable_jobs = [j for j in jobs if j[1] == t]
        if executable_jobs:
            opt[t] = max(opt[t - 1], max([j[2] + opt[j[0]] for j in executable_jobs]))
        else:
            opt[t] = opt[t - 1]
    return max(opt), opt


if __name__ == '__main__':
    # (start, end, weight)
    jobs = [(0, 2, 3), (2, 10, 3), (1, 4, 6), (4, 7, 4), (9, 10, 3), (3, 4, 2)]
    print(weighted_interval_scheduling(jobs))

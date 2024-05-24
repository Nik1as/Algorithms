def list_scheduling(jobs, m):
    machines = [0] * m
    for job in jobs:
        i = machines.index(min(machines))
        machines[i] += job
    return max(machines)


def longest_jobs_first_scheduling(jobs, m):
    return list_scheduling(sorted(jobs, reverse=True), m)


if __name__ == '__main__':
    jobs = [1, 2, 5, 8, 2, 4]
    m = 2
    print(list_scheduling(jobs, 2))
    print(longest_jobs_first_scheduling(jobs, m))

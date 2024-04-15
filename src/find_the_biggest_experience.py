from src.priority_queue_for_binnary_tree import PriorityQueue

def max_experience(levels, experience):
    max_exp = 0
    for i in range(levels):
        priority_queue = PriorityQueue()

        for j in range(i, -1, -1):
            priority_queue.add_task(experience[i][j], -experience[i][j])

        level_max_exp = 0
        for _ in range(i + 1):  
            task = priority_queue.remove_highest_priority_task()
            if task:
                _, priority = task
                level_max_exp += -priority
            else:
                break

        max_exp += level_max_exp

    return max_exp

def main():
    with open("career_lab.in", "r") as f:
        levels = int(f.readline())
        experience = []
        for i in range(levels):
            line = list(map(int, f.readline().split()))
            experience.append(line)

    max_exp = max_experience(levels, experience)

    with open("career_lab.out", "w") as f:
        f.write(str(max_exp))

if __name__ == "__main__":
    main()
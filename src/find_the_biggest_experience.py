##6
def maximum_experience(levels, organization):
    max_experience = 0
    queue = [(0, 0)]
    while queue:
        level, experience = queue.pop(0)
        max_experience = max(max_experience, experience)
        if level < levels:
            for next_level, next_experience in enumerate(organization[level], start=1):
                queue.append((level + 1, experience + next_experience))
    return max_experience

def main():
    with open('career_lab.in', 'r') as f:
        levels = int(f.readline())
        organization = []
        for _ in range(levels):
            organization.append(list(map(int, f.readline().split())))

    max_experience = maximum_experience(levels, organization)

    with open('career_lab.out', 'w') as f:
        f.write(str(max_experience))

if __name__ == "__main__":
    main()
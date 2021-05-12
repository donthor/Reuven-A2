def family_ages(agefile, **people):
    with open(agefile, 'w') as f:
        for person, age in sorted(people.items(), reverse=True):
            f.write(person + ',' + str(age) + '\n')
    f = open(agefile, 'r')
    print(f.read())
family_ages('ages.txt', Benjamin = 1, Patrick = 2, Paul = 4)
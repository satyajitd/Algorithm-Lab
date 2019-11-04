import random
import matplotlib.pyplot as plt

def solve(n_students, n_companies):
    pref = []
    result = {}
    visit = {}
    first_pref = 0

    for i in range(n_companies):
        visit[i+1] = False

    for i in range(n_students):
        student_pref = list(range(1, n_companies+1))
        random.shuffle(student_pref)
        student_pref.append(i+1)
        pref.append(student_pref)

    # Allocate
    for _ in range(n_students):
        # Student
        i = random.randrange(0, len(pref))
        for j in range(n_companies):
            if(not visit[pref[i][j]]):
                result[pref[i][-1]] = pref[i][j]
                visit[pref[i][j]] = True
                if(j == 0):
                    first_pref = first_pref + 1
                break
        del pref[i]   

    return first_pref

if __name__ == "__main__":

    x = []
    y = []
    for i in range(50, 301, 50):
        x.append(i)
        y.append(solve(i, i))
    plt.scatter(x, y)
    plt.xlabel('No. of Students/Companies')
    plt.ylabel('No. of Students who got their first preference')
    plt.show()

import sys

def solve(grades):
    # Complete this function
    new_grades = [];
    for i in grades:
        if i < 38:
            new_grades.append(i)
        elif abs((i-((i//5+1)*5))) < 3:
            new_grades.append((i//5+1)*5)
            print("appended:", (i//5+1)*5)
        else:
            new_grades.append(i)
    return new_grades

TEST_CASE = [4, 67, 73, 38, 33]
print(solve(TEST_CASE))

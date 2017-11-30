# bisect acts like bisect(haystack, needle) 
import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score) 
    return grades[i]

if __name__ == "__main__":
    result = [grade(score) for score in [33, 63, 99, 70, 81]]
    print(result) 

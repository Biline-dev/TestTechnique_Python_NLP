def solution(s):

    idx = len(s)//2

    if len(s)%2 ==0 or s[idx+1:][::-1] != s[:idx]: 
        return -1
    elif len(s)<2:
        return 0
    else:
        return idx

print(solution("racecar")) # 3
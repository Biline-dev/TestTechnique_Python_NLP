

"""
* La fonction calculate_result vérifie si les conditions nécessaires pour le calcul sont remplies.
* Si les conditions ne sont pas satisfaites, une ValueError est levée avec un message approprié.
* La fonction solution utilise un algorithme pour construire une chaîne de caractères résultante 
en fonction des valeurs de A et B.
"""


def calculate_result(A, B):
    if A % 2 == B % 2 == 0 and (B < A // 2 - 1 or A < B // 2 - 1):
        raise ValueError("Impossible de calculer : B ou A trop petit")
    elif A % 2 == B % 2 != 0 and (B < A // 2 or A < B // 2):
        raise ValueError("Impossible de calculer : B ou A trop petit")

        
def solution(A, B):
    
    result = ""

    try:
        calculate_result(A, B)

        while A > 0 or B > 0:
            if A > B:
                if result[-2:] != 'aa' and A > 0:
                    result += 'a'
                    A -= 1
                elif result[-2:] != 'bb' and B > 0:
                    result += 'b'
                    B -= 1
            else:
                if result[-2:] != 'bb' and B > 0:
                    result += 'b'
                    B -= 1
                elif result[-2:] != 'aa' and A > 0:
                    result += 'a'
                    A -= 1
    except ValueError as e:
        print(e)

    return result

# Tests
print(solution(7, 1)) # "aabbaaba"
print(solution(5, 3)) # "aabbaaba"
print(solution(6, 5)) # "aabbaaba"
print(solution(5, 2)) # "aabaaba"
print(solution(7, 3)) # "aabaabaaba"
print(solution(7, 6)) # "aabbaabbaabba"
print(solution(3, 3)) # "bbaaba"
print(solution(1, 4)) # "bbabb"


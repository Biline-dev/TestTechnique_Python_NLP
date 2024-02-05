def solution(a):
    # Calculer la taille du tableau
    taille = len(a)

    # Cas où il y a un seul élément dans le tableau
    if taille == 1:
        return abs(a[0] * 2)
    
    # Cas où le tableau est vide
    if taille < 1:
        return None

    # Trier le tableau
    sorted_array = sorted(a)

    # Cas où tous les éléments sont négatifs
    if sorted_array[-1] <= 0:
        return abs(sorted_array[-1] * 2)
    # Cas où tous les éléments sont positifs
    elif sorted_array[0] >= 0:
        return sorted_array[0] * 2
    else:
        # Cas où il y a un mélange d'éléments positifs et négatifs
        debut, fin = 0, taille - 1
        min_somme = float('inf')

        while debut < fin:
            somme = sorted_array[debut] + sorted_array[fin]
            min_somme = min(min_somme, abs(somme))

            if somme < 0:
                debut += 1 
            elif somme > 0:
                fin -= 1
            else:
                return 0
        
        return min_somme

# Test du code avec un exemple
exemple_test = [3, -4, 5, -2, 7, -1]
resultat = solution(exemple_test)
print("Résultat du test :", resultat)

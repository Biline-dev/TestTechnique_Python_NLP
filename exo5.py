from collections import deque

def parcours(matrice, debut, visite):
    
    
    queue = deque([debut])  # on utilise une file pour parcours les regions
    visite[debut[0]][debut[1]] = True # on marque chaque region visité

    nb_raw, m_col= len(matrice), len(matrice[0]) 
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # nord, sud, est, ouest
 
    while queue:  # si la file est vide, cela voudrai dire qu'on a fini l'exploration de ce pays
        x, y = queue.pop() 
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < nb_raw and 0 <= new_y < m_col and not visite[new_x][new_y] and matrice[new_x][new_y] == matrice[x][y]:
                # une fois la region exploré, on la rajoute à la file pour en explorer d'autres à partir de cette region
                queue.append((new_x, new_y)) 
                visite[new_x][new_y] = True

def solution(matrice):
    nb_raw, m_col = len(matrice), len(matrice[0])
    visite = [[False] * m_col for _ in range(nb_raw)]
    countries = 0 # compteur 

    for i in range(nb_raw):
        for j in range(m_col):
            if not visite[i][j]: # on visite seulement les regions non explorées
                parcours(matrice, (i, j), visite)
                countries += 1

    return countries

# Test :
matrice = [
    [5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 1],
    [1, 4, 4],
    [4, 1, 1]
]

result = solution(matrice)
print(result)  # 12

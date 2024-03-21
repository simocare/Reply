from heapq import heappop, heappush

# Funzione per trovare il percorso più breve tra due punti utilizzando Dijkstra
def trova_percorso(piattaforma, inizio, fine, width, height):
    punti = {(x, y): float('inf') for x in range(width) for y in range(height)}
    punti[inizio] = 0
    coda = [(0, inizio, [])]

    while coda:
        costo, attuale, percorso = heappop(coda)

        if attuale == fine:
            return percorso

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = attuale[0] + dx, attuale[1] + dy
            if 0 <= x < width and 0 <= y < height and piattaforma[y][x] != 'G':
                nuovo_costo = costo + 1
                nuovo_punto = (x, y)
                if nuovo_costo < punti[nuovo_punto]:
                    punti[nuovo_punto] = nuovo_costo
                    heappush(coda, (nuovo_costo, nuovo_punto, percorso + [nuovo_punto]))

# Funzione per calcolare il percorso massimo e stamparlo sulla matrice
def stampa_percorso_massimo(matrice, punti, inizio, fine, width, height):
    # Copia della matrice originale
    nuova_matrice = [riga[:] for riga in matrice]

    # Calcolo del percorso massimo
    percorso = trova_percorso(nuova_matrice, inizio, fine, width, height)

    # Aggiunta del percorso alla matrice
    for x, y in percorso:
        if nuova_matrice[y][x] == '.':
            nuova_matrice[y][x] = '*'

    # Stampa della matrice con il percorso inserito e mantenimento dei punti
    for y in range(len(nuova_matrice)):
        for x in range(len(nuova_matrice[y])):
            if (x, y) in punti:
                print(f'{punti[(x, y)]:<4}', end='')
            else:
                print(f'{nuova_matrice[y][x]:<4}', end='')
        print()

# Creazione della matrice con larghezza e altezza specificate
def crea_matrice(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

# Definizione dei punti e delle loro coordinate
punti = {
    (4, 4): 100,
    (4, 2): 100,
    (6, 0): 150,
    (7, 5): 150,
    (2, 4): 1,
    (7, 2): 2,
    (6, 6): 3
}

# Definizione della larghezza e altezza della matrice
width = 10
height = 7

# Creazione della matrice
matrice = crea_matrice(width, height)

# Stampa del percorso da 1 a 2
print("Percorso da 1 a 2:")
stampa_percorso_massimo(matrice, punti, (2, 4), (7, 2), width, height)
print()

# Stampa del percorso da 1 a 3
print("Percorso da 1 a 3:")
stampa_percorso_massimo(matrice, punti, (2, 4), (6, 6), width, height)
print()

# Stampa del percorso da 2 a 3
print("Percorso da 2 a 3:")
stampa_percorso_massimo(matrice, punti, (7, 2), (6, 6), width, height)

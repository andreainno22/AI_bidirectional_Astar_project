def get_map(file_name, start_row, r, c):
    with open(file_name, 'r') as file:
        righe = file.readlines()

    # Unisci le righe da riga_inizio in poi in una singola stringa
    string = ''.join(riga.strip() for riga in righe[start_row - 1:])

    def string_to_matrix(string, r, c):
        # Crea una matrice vuota
        matrix = [['' for _ in range(c)] for _ in range(r)]

        # Controlla se la stringa può essere inserita nella matrice
        if len(string) > r * c:
            print("La stringa è troppo lunga per la matrice specificata.")
            return matrix

        # Inserisci i caratteri della stringa nella matrice
        index = 0
        for i in range(r):
            for j in range(c):
                if index < len(string):
                    matrix[i][j] = string[index]
                    index += 1
        return matrix

    return string_to_matrix(string, r, c)

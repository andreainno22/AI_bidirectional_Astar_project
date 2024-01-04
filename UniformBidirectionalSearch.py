from queue import PriorityQueue

class Nodo:
    def __init__(self, valore, costo=0):
        self.valore = valore
        self.costo = costo
        self.genitore = None

class Grafo:
    def __init__(self):
        self.nodi = {}

    def aggiungi_nodo(self, nodo):
        self.nodi[nodo.valore] = nodo

    def get_nodo(self, valore):
        return self.nodi[valore]

    def get_vicini(self, nodo):
        # Questo metodo dovrebbe essere implementato in base alla struttura del tuo grafo
        pass

def ricerca_bidirezionale(grafo, inizio, fine):
    coda_inizio = PriorityQueue()
    coda_fine = PriorityQueue()

    coda_inizio.put((inizio.costo, inizio))
    coda_fine.put((fine.costo, fine))

    visitati_inizio = {inizio}
    visitati_fine = {fine}

    while not coda_inizio.empty() and not coda_fine.empty():
        _, nodo_inizio = coda_inizio.get()
        _, nodo_fine = coda_fine.get()

        if nodo_inizio in visitati_fine or nodo_fine in visitati_inizio:
            return nodo_inizio, nodo_fine

        for vicino in grafo.get_vicini(nodo_inizio):
            if vicino not in visitati_inizio:
                vicino.costo = nodo_inizio.costo + 1  # Supponiamo che tutti i bordi abbiano costo 1
                vicino.genitore = nodo_inizio
                coda_inizio.put((vicino.costo, vicino))
                visitati_inizio.add(vicino)

        for vicino in grafo.get_vicini(nodo_fine):
            if vicino not in visitati_fine:
                vicino.costo = nodo_fine.costo + 1  # Supponiamo che tutti i bordi abbiano costo 1
                vicino.genitore = nodo_fine
                coda_fine.put((vicino.costo, vicino))
                visitati_fine.add(vicino)

    return None, None
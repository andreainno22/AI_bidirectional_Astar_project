"""implementa una coda con priorità con tempo di O(nlogn) per l'inserimento e O(1) per l'estrazione"""
from timeit import default_timer as timer


class PriorityList:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def put(self, data):
        self.list.append(data)
        start = timer()
        self.list.sort(key=lambda x: x[0], reverse=False)
        end = timer()
        time = end - start

    def get(self):
        if self.is_empty():
            return "La coda è vuota"
        else:
            return self.list.pop(0)  # rimuove e restituisce l'elemento con la priorità più alta

    def first_element(self):
        return self.list[0]

    def empty(self):
        if self.is_empty():
            return True

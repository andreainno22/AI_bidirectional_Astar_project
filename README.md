In questo file sono descritte le funzione e le classi principali dell'esercizio e le loro funzionalità. Per riprodurre i risultati riportati nella relazione è necessario 
scaricare le mappe dai seguenti link: 
https://www.movingai.com/benchmarks/bgmaps/bgmaps-map.zip (mappa AR0011SR) , https://www.movingai.com/benchmarks/wc3maps512/wc3maps512-map.zip (mappa battleground e plainsofsnow),
e i relativi scenari https://www.movingai.com/benchmarks/bgmaps/bgmaps-scen.zip e https://www.movingai.com/benchmarks/wc3maps512/wc3maps512-scen.zip. 
Una volta scaricate le mappe è necessario inserire la mappa nella rispettiva directory creata con lo stesso nome della mappa e poi nella directory 'maps'
(es: maps/battleground/battleground.map). Una volta fatto ciò è sufficiente eseguire il main.

File sorgenti:

BidirectionalSearchAstar.py : all'interno della classe BidirectionalSearchAstar viene implementato il metodo '
bidirectional_search_Astar()', che riceve un oggetto AstarGraphProblem e una stringa che indica il
tipo di frontiera, che può essere 'basic' (di default), che equivale a utilizzare una Prioritylist (spiegata in
seguito), o 'heap', per cui invece la frontiera viene inizializzata come PriorityQueue
della libreria 'queue' di python, implementata con binary heap e quindi con un tempo costante di estrazione e logaritmico di inserimento.

UnidirectionalAearchAstar.py: al suo interno viene implementata la funzione 'unidirectional_search_Astar', che riceve gli stessi input di 'bidirectional_search_Astar()'.

AstarGraphProblem.py: contiene la classe 'AstarGraphProblem' che fornisce i seguenti metodi:
  ° def __init__(self, initial, goal, graph, heuristic=None) : nel costruttore viene inizializzato lo stato iniziale (self.initial), lo stato goal (self.goal), l'euristica
(heuristic) che di default è nulla, e la matrice di adiacenza (self.nodes).

  ° def actions(self, state) : per calcolare le azioni effettuabili dall'agente dato uno stato di partenza (x,y), scegliendole tra UP, DOWN, LEFT, RIGHT, UPLEFT, UPRIGHT, 
    DOWNLEFT, DOWNRIGHT. Il calcolo delle azioni effettuabili viene fatto in base alla matrice di adiacenza che rappresenta la mappa (self.nodes): in particolare, un'azione sarà 
    effettuabile se in quella direzione vi è un 1 nella matrice.

° def result(self, node, action) : dato un nodo, ritorna lo stato del nodo risultante da quell'azione.

° def h(self, currentNode, goalNodeState) : viene effettuato il calcolo dell'euristica nello stato del currentNode, dato
lo stato goal che può essere self.initial oppure self.goal a seconda
dei casi nella ricerca bidirezionale, solo self.goal nella ricerca unidirezionale.

° def effective_path_cost(self, c, action) : calcola l’effettivo path cost, serve per ottenere la soluzione finale

° def path_cost_bi(self, c, node1, action, node2) : dato il costo per raggiungere lo stato node1.state, si calcola il
path_cost di node2 come
c + 1 + 0.5 * (self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(node2, self.initial)) nel caso di mossa verticale o orizzontale, 
    c + 2 ** 0.5 + 0.5 * (self.h(node1, self.initial) - self.h(node1, self.goal) + self.h(node2, self.goal) - self.h(node2, self.initial)) nel caso di mossa diagonale. 
    Tale path_cost è giustificato dalle considerazioni fatte in questo articolo https://onlinelibrary.wiley.com/doi/abs/10.1002/net.20131, sezione 5.2.

° def path_cost_un(self, c, node1, action, node2) : come per la versione bidirezionale, in quella unidirezionale il
calcolo del costo viene fatto secondo la formula:
c + 1 + 0.5 * (self.h(node1, self.goal) - self.h(node2, self.goal)) nel caso di mossa verticale o orizzontale,
c + 2 ** 0.5 + 0.5 * (self.h(node1, self.goal) - self.h(node2, self.goal)) nel caso di mossa diagonale.
Tale path_cost è giustificato dalle considerazioni fatte in questo
articolo https://onlinelibrary.wiley.com/doi/abs/10.1002/net.20131, sezione 5.2.
    
  ° def get_neighbors_bi(self, node) : dato un nodo, restituisce i vicini di quel nodo, inizializzandoli e assegnando loro il path cost necessario per raggiungerli (tramite la
    funzione 'path_cost_bi()').

  ° def get_neighbors_un(self, node), def path_cost_un(self, c, node1, action, node2) : svolgono la stessa funzione del caso bidirezionale nel caso unidirezionale.

Node.py: in questo file è implementata la classe Node, che ha i seguenti metodi:
  ° def __init__(self, state, parent=None, parent2=None, action=None, path_cost=0): inizializza stato, genitori (nel caso in cui, nella ricerca bidirezionale, il nodo in questione
  sia il nodo di intersezione fra le due frontiere, gli viene assegnato il doppio padre così da poter ricostruire la soluzione in entrambi in versi), azione compiuta per crearlo, 
  path_cost e profondità (self.depth = parent.depth + 1)

  ° def path(self) : ricostruisce il percorso che ha portato a quel nodo come lista di stati.

PriorityList.py : in questo file è implementata la classe PriorityList una lista con priorità, che restituisce in tempo
costante (O(1)) l'elemento a più alta priorità, mentre impiega
un tempo O(nlogn) per l'inserimento, dato che ogni volta che viene inserito un nuovo valore deve essere effettuato un
ordinamento degli elementi della lista.

StringToMatrix.py : in questo file è implementata la funzione def get_map(file_name, start_row, r, c), che, dato il nome del file, la riga di inizio da cui leggere, la lunghezza
(r) e la larghezza (c) del file, restituisce una matrice (rxc), che rappresenta la matrice di adiacenza del grafo che
rappresenta la mappa. In particolare, la matrice avrà un 1 in ogni
coordinata in cui nel grafo vi è uno dei seguenti simboli: '.','G','S','W', e uno 0 altrimenti.

main.py : vengono convertite le tre mappe in matrici e per ogni mappa vengono eseguiti 12 test (un totale di 36 test): viene eseguita la ricerca bidirezionale sulla mappa
dato uno scenario, che corrisponde a un punto di partenza e un goal, con frontiera implementata come PriorityQueue o
PriorityList e con euristica nulla, euclidea o
manhattan, stessa cosa viene fatta con la ricerca unidirezionale. Per ogni test viene stampato il percorso compiuto, il
costo totale del percorso, il numero di iterazioni
effettuate dall'algoritmo e il tempo impiegato.


  

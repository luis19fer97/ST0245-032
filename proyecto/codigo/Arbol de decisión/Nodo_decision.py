# En este método se crea un nodo de decisón con una pregunta asociada
"""
    Un nodo de decisión hace una pregunta.
    Esto contiene una referencia a la pregunta y a los dos nodos hijos.
"""
class nodo_decision:
    def __init__(self,
                 pregunta,
                 rama_verdadera,
                 rama_falsa):
        self.pregunta = pregunta
        self.rama_verdadera = rama_verdadera
        self.rama_falsa = rama_falsa
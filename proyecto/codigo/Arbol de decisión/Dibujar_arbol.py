from Hoja import hoja
from Preguntas import pregunta

# Este método permite dibujar el árbol de una manera entendible en la consola
# tomado de: https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb
# Youtube: Google developers
# Let’s Write a Decision Tree Classifier from Scratch - Machine Learning Recipes #8

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, hoja):
        print (spacing + "Predict", node.prediccion)
        return

    # Print the question at this node
    print (spacing + str(node.pregunta))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.rama_verdadera, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.rama_falsa, spacing + "  ")

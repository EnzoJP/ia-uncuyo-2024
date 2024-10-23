import csv

class Node:
    def __init__(self, attribute=None, classification=None):
        self.attribute = attribute
        self.classification = classification
        self.children = {}

#------------------------------------------------------------

def decision_tree_learning(examples, attributes, parent_examples=None):
    if len(examples) == 0:
        return Node(classification=plurality_value(parent_examples))
    elif same_classification(examples):
        return Node(classification=examples[0]['play'])
    elif len(attributes) == 0:
        return Node(classification=plurality_value(examples))
    else:
        A = choose_attribute(attributes, examples)
        tree = Node(attribute=A)
        for val in set(e[A] for e in examples):
            exs = [e for e in examples if e[A] == val]
            subtree = decision_tree_learning(exs, [a for a in attributes if a != A], examples)
            tree.children[val] = subtree
        return tree
    
def same_classification(examples):
    # retorna True si todos los ejemplos tienen la misma clasificación
    classification = examples[0]['play'] 
    for e in examples:
        if e['play'] != classification:
            return False
    return True


def plurality_value(examples):
    # Retorna la clasificación más común en los ejemplos
    list_of_classifications_count = []
    classifications = [e['play'] for e in examples]  
    
    for classification in classifications:
        count = classifications.count(classification) 
        
        if count > len(examples) / 2:  # hay mayoría 
            return classification
        
        list_of_classifications_count.append(count)
    
    # clasificación más común
    max_count_index = list_of_classifications_count.index(max(list_of_classifications_count))
    return classifications[max_count_index]

    
import math

def entropy(examples):
    total = len(examples)
    positive = sum(1 for e in examples if e['play'] == 'yes')
    negative = total - positive
    if positive == 0 or negative == 0:
        return 0
    p_positive = positive / total
    p_negative = negative / total
    return - (p_positive * math.log2(p_positive) + p_negative * math.log2(p_negative)) #formula de entropía

def information_gain(examples, attribute):
    total_entropy = entropy(examples)
    values = set(e[attribute] for e in examples)
    weighted_entropy = 0
    for value in values:
        subset = [e for e in examples if e[attribute] == value]
        weighted_entropy += len(subset) / len(examples) * entropy(subset) # Resto
    return total_entropy - weighted_entropy # cuanto de la entropía total se reduce al considerar el atributo

def choose_attribute(attributes, examples):
    best_gain = -1
    best_attribute = None
    for attribute in attributes:
        gain = information_gain(examples, attribute)
        if gain > best_gain:
            best_gain = gain
            best_attribute = attribute
    return best_attribute

#------------------------------------------------------------
def load_dataset(filename):
    examples = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            examples.append(row)
    return examples

examples = load_dataset("tp7-ml/code/id3/tennis.csv") # filas de la tabla pero como diccionarios :o

attributes = ["outlook", "temp", "humidity", "windy"] # columnas de la tabla (menos la clasificación)

tree = decision_tree_learning(examples, attributes)

def print_tree(node, indent=""):
    if node.attribute is not None:
        # Imprimir el nodo atributo
        print(indent + "Atributo: " + str(node.attribute))
        for value, child in node.children.items():
            # Imprimir los valores de las ramas
            print(indent + "  └── Valor: " + str(value))
            # Recursivamente imprimir el subárbol con mayor indentación
            print_tree(child, indent + "      ")
    else:
        # Si no hay atributo, es una hoja. Imprimir la clasificación
        print(indent + "  └── Clasificación: " + str(node.classification))


print_tree(tree)







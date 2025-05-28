def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    longitud = len(lista)
    
    if longitud >= 6:
        del lista[5]
    
    if longitud >= 5:
        del lista[4]
  
    if longitud >= 1:
        del lista[0]
    return lista



def add_elements(list_to_add_elements):
    lista2 = list_to_add_elements

    lista2.insert(0, "Pink")
    lista2.insert(len(lista2), "Yellow")

    return lista2


def is_empty(list_to_check):

    
    longitud = len(list_to_check)
    lista = longitud == 0

    return lista

def check_lists(list_to_compare1, list_to_compare2):
    lista = list_to_compare1
    lista2 = list_to_compare2


    if len(lista) >= 3 and len(lista2) >= 3:
        if lista[2] == lista2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):

    listagrande = list_of_lists_to_modify
    lista1 = listagrande[0]
    lista1 = lista1[0:2]
    lista2 = listagrande[1]
    lista2 = lista2[1:4]
    lista3 = listagrande[2]
    lista3 = lista3[-2:]

    listagrande = [lista1, lista2, lista3]


    return listagrande

def read_list():
    ''' Citirea unei liste de numere întregi
        Input:nr=câte numere să conțină lista
              numerele din listă
        Output:Lista cu numere
    '''
    list = []
    n = int(input("Lungimea listei este: "))
    element = int(input("Dați primul element "))
    list.append(element)
    for i in range(1, n):
        element = int(input("Dați al {}-lea element ".format(i + 1)))
        list.append(element)
    return list

def numere_negative_nenule (list):
    '''
    Determină toate numerele negative nenule din listă
    :param list: lista de numere întregi
    :return: Returnează numerele negative nenule din lista dată
    '''
    rez = []
    for x in list:
        if x!=0 and x<0:
         rez.append(x)
    return rez

def test_numere_negative_nenule():
    assert numere_negative_nenule([-1, -56, 0, 7]) == [-1,-56]
    assert numere_negative_nenule([2,5,18,-23]) == [-23]
    assert numere_negative_nenule([1,2,9.10]) == []

def show_menu():
    print("1.Citire listă")
    print("2.Afișarea tuturor numerelor negative nenule din listă ")
    print("x.Ieșire")

def main():
    list = []
    while True:
        show_menu()
        op = input("Opțiune: ")
        if op == "1":
            list = read_list()
        elif op == "2":
            print(numere_negative_nenule(list))
        elif op == "x":
            break
        else:
            print("Opțiune invalidă")
main()

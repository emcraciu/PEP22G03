
def adaugare_func():
    from app1 import inventar
    produse = input("ce produse doriti sa adaugati?:  ").split(",")
    inventar.update({produse[0]: (produse[1], produse[2])})

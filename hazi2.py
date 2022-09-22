



def triangle():
    print("Adja meg a háromszög három oldalát cm-ben:")

    a = int(input("a oldal (cm) : "))
    b = int(input("b oldal (cm) : "))
    c = int(input("c oldal (cm) : "))

    if a + b > c and  a + c > b and c+b > a:
        print("A {} {} {} oldalú háromszög szerkeszthető!".format(a,b,c))
    else:
        print("A {} {} {} oldalú háromszög NEM szerkeszthető!".format(a,b,c))



if __name__ == "__main__":
    triangle()
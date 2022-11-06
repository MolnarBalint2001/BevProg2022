



def szorzo_tabla(n):
    
    
    numbers = [int(x) for x in range (1,n)]
    multipliers  = [int(x) for x in range (1,n)]
    

    for x in multipliers:
        
        print("{}:".format(x), end=" ")
        for y in numbers:
            line = "\t{}"

            print(line.format(x*y),end="")
        print()




isPalindrome = lambda s: s==s[::-1]


if __name__ == "__main__":
    szorzo_tabla(13)
    print(isPalindrome("arany nyara"))
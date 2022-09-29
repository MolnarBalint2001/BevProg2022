
from warnings import catch_warnings

def main():
    a = int(input("Enter 'a' value: "))
    b = int(input("Enter 'a' value: "))

    try:
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Division by zero is not allowed!")

    print("Out of try execpt block!")
if __name__ == "__main__":
    while True:
        main()
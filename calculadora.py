from sys import exit
import sys


def main():
    if len(sys.argv) != 4:
        print("Erro parametros")
        exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    op = sys.argv[3]
    
    if op == "add":
        print(str(num1+num2))
        exit(0)
    if op == "sub":
        print(str(num1-num2))
        exit(0)
    if op == "mul":
        print(str(num1*num2))
        exit(0)
    if op == "div":
        print(str(num1/num2))
        exit(0)
    
    print("Erro op")
    exit(1)

if __name__ == "__main__":
    main()
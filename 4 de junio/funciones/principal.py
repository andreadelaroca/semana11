import operaciones as paputilin

def main():
    while True:
        print("\nIntroduzca los valores que utilizará:")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("\nSeleccione una operación:")
        paputilin.menu()
        op = input("\nDigite una opción: ")
        if op == "1":
            resultado = (paputilin.sumar(num1, num2))
            print(f"Suma: {resultado}")
        elif op == "2":
            resultado = (paputilin.restar(num1, num2))
            print(f"Resta: {resultado}")
        elif op == "3":
            resultado = (paputilin.multiplicar(num1, num2))
            print(f"Multiplicación: {resultado}")
        elif op == "4":
            resultado = int(paputilin.dividir(num1, num2))
            print(f"División: {resultado}")
        elif op == "5":
            x = int(input("Ingrese el valor de x: "))
            y = int(input("Ingrese el valor de y: "))
            z = int(input("Ingrese el valor de z: "))
            mult = paputilin.multiplicar(2, y)
            sum = paputilin.sumar(x, mult)
            div = paputilin.dividir(sum, z)
            print(div)
        else:
            break
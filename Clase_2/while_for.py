def run():
    n = int(input("Ingresa un número: "))
    for elemento in range(2, n):
        if n % elemento == 0:
            print("No es primo")
            break
        else: 
            print()


if __name__ == "__main__":
    run()




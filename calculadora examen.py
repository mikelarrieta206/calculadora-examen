import itertools

while True:
    print("\n===== CALCULADORA LÓGICA Y MATEMÁTICA =====")
    print("1. Operaciones matemáticas")
    print("2. Operaciones con conjuntos")
    print("3. Operaciones lógicas")
    print("4. Clasificación lógica")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    # =========================
    # 1. OPERACIONES MATEMÁTICAS
    # =========================
    if opcion == 1:
        print("\n--- OPERACIONES MATEMÁTICAS ---")

        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")

        op = int(input("Seleccione una operación: "))

        if op == 1:
            print("Resultado:", a + b)
        elif op == 2:
            print("Resultado:", a - b)
        elif op == 3:
            print("Resultado:", a * b)
        elif op == 4:
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: División entre cero")
        elif op == 5:
            print("Resultado:", a ** b)
        else:
            print("Opción inválida")

    # =========================
    # 2. OPERACIONES CON CONJUNTOS
    # =========================
    elif opcion == 2:
        print("\n--- OPERACIONES CON CONJUNTOS ---")

        A = set(map(int, input("Ingrese A separados por comas: ").split(",")))
        B = set(map(int, input("Ingrese B separados por comas: ").split(",")))

        print("\nConjunto A:", A)
        print("Conjunto B:", B)

        print("\nUnión (A ∪ B):", A | B)
        print("Intersección (A ∩ B):", A & B)
        print("Diferencia (A - B):", A - B)
        print("Diferencia simetrica (A △ B):", A ^ B)

        producto = {(a, b) for a in A for b in B}
        print("Producto cartesiano (A × B):", producto)

        print("Cardinalidad de A:", len(A))
        print("Cardinalidad de B:", len(B))

    # =========================
    # 3. OPERACIONES LÓGICAS
    # =========================
    elif opcion == 3:
        print("\n--- OPERACIONES LÓGICAS ---")

        p_input = input("Ingrese p (True/False): ").strip().lower()
        q_input = input("Ingrese q (True/False): ").strip().lower()

        if p_input not in ["true", "false"] or q_input not in ["true", "false"]:
            print("Error: debe ingresar True o False")
        else:
            p = p_input == "true"
            q = q_input == "true"

            print("\nResultados de las operaciones lógicas")
            print("Conjunción (p AND q):", p and q)
            print("Disyunción (p OR q):", p or q)
            print("Negación (NOT p):", not p)
            print("Condicional (p → q):", (not p) or q)
            print("Bicondicional (p ↔ q):", p == q)

    # =========================
    # 4. CLASIFICACIÓN LÓGICA
    # =========================
    elif opcion == 4:
        print("\n--- CLASIFICACIÓN LÓGICA ---")
        print("Tabla de verdad para (p AND q) -> p\n")

        resultados = []

        for p, q in itertools.product([True, False], repeat=2):
            expresion = (not (p and q)) or p
            resultados.append(expresion)
            print("p =", p, "q =", q, "resultado =", expresion)

        if all(resultados):
            print("\nLa expresión es una TAUTOLOGÍA")
        elif not any(resultados):
            print("\nLa expresión es una CONTRADICCIÓN")
        else:
            print("\nLa expresión es una CONTINGENCIA")

    # =========================
    # 5. SALIR
    # =========================
    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intente de nuevo.")
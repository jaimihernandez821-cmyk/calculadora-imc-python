# --- INPUT DE STRINGS ---
# Usamos la función built-in input() para capturar secuencias de caracteres.
nombre = input("Nombre: ")
paterno = input("Apellido Paterno: ")
materno = input("Apellido Materno: ")

# --- CONTROL DE FLUJO Y CASTEO ---
try:
    # Aplicamos lógica booleana para verificar que los strings no estén "falsy" (vacíos)
    if not nombre or not paterno or not materno:
        print("Error: Los nombres no pueden quedar vacíos.")
    else:
        # Hacemos 'casting' (conversión de tipo) de string a int y float
        edad = int(input("Edad: "))
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))

        # Operación aritmética con el operador de potencia (**)
        imc = peso / (estatura ** 2)

        # --- OUTPUT CON F-STRINGS ---
        # Usamos f-strings (literales de cadena formateados) para una interpolación limpia
        print("\n" + "="*30)
        print(f"USUARIO: {nombre} {paterno} {materno}")
        print(f"EDAD: {edad} años")
        # El modificador :.2f redondea el float a dos decimales
        print(f"IMC CALCULADO: {imc:.2f}")
        print("="*30)

except ValueError:
    # Manejo de excepciones para evitar que el programa se rompa (crash) por tipos de datos incompatibles
    print("Error: Edad, Peso y Estatura deben ser cifras numéricas.")
"""
CONVERSOR BINARIO - Laboratorio de Sistemas Embebidos
Convierte números binarios a decimal, octal y hexadecimal
"""

def validar_binario(numero):
    """Función para validar que el número ingresado sea binario"""
    for digito in numero:
        if digito not in ['0', '1']:
            return False
    return True

def binario_a_decimal(numero_binario):
    """Convierte un número binario (string) a decimal (int) manualmente"""
    decimal = 0
    longitud = len(numero_binario)
    
    for i, digito in enumerate(numero_binario):
        posicion_desde_derecha = longitud - 1 - i
        if digito == '1':
            decimal += 2 ** posicion_desde_derecha
    
    return decimal

def mostrar_resultados(binario, decimal, octal, hexadecimal):
    """Muestra los resultados de forma organizada"""
    print("\n" + "="*40)
    print("RESULTADOS DE LA CONVERSIÓN")
    print("="*40)
    print(f"Número binario ingresado: {binario}₂")
    print(f"En decimal (base 10): {decimal}₁₀")
    print(f"En octal (base 8): {octal}₈")
    print(f"En hexadecimal (base 16): {hexadecimal}₁₆")
    print("="*40)

def main():
    """Función principal del programa"""
    print("\n" + "="*50)
    print("🔢 CONVERSOR DE NÚMEROS BINARIOS 🔢")
    print("="*50)
    print("Este programa convierte números binarios a:")
    print("• Decimal (base 10)")
    print("• Octal (base 8)")
    print("• Hexadecimal (base 16)")
    print("-"*50)
    
    while True:
        # Solicitar número binario al usuario
        numero_binario = input("\n📥 Ingresa un número binario (ej: 1010): ").strip()
        
        # Validar que sea binario
        if not validar_binario(numero_binario):
            print("❌ ERROR: El número debe contener solo 0s y 1s.")
            continue
        
        # Mostrar el número ingresado
        print(f"\n✅ Número válido: {numero_binario}")
        
        # MÉTODO 1: Conversión manual
        print("\n--- Método manual (cálculo paso a paso) ---")
        decimal_manual = binario_a_decimal(numero_binario)
        
        # Mostrar el proceso
        for i, digito in enumerate(numero_binario):
            pos = len(numero_binario) - 1 - i
            if digito == '1':
                print(f"  {digito} × 2^{pos} = {2**pos}")
        print(f"  Suma total = {decimal_manual}")
        
        # MÉTODO 2: Conversión con Python
        print("\n--- Método con funciones de Python ---")
        decimal_python = int(numero_binario, 2)
        octal_python = format(decimal_python, 'o')
        hex_python = format(decimal_python, 'X')
        
        print(f"Usando int('{numero_binario}', 2) = {decimal_python}")
        print(f"Octal: {octal_python}")
        print(f"Hexadecimal: {hex_python}")
        
        # Mostrar resultados
        mostrar_resultados(numero_binario, decimal_python, octal_python, hex_python)
        
        # Preguntar si desea continuar
        respuesta = input("\n¿Quieres convertir otro número? (s/n): ").lower()
        if respuesta != 's':
            print("\n👋 ¡Gracias por usar el conversor binario!")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    main()

def menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("      CONVERSOR BINARIO - MENÚ")
    print("="*40)
    print("1. Convertir binario a decimal")
    print("2. Convertir binario a octal")
    print("3. Convertir binario a hexadecimal")
    print("4. Convertir binario a TODOS los sistemas")
    print("5. Ayuda (explicación de conversiones)")
    print("6. Salir")
    print("="*40)

def mostrar_ayuda():
    """Muestra ayuda sobre conversiones"""
    print("\n📚 AYUDA: CONVERSIÓN DE NÚMEROS BINARIOS")
    print("-"*40)
    print("BINARIO → DECIMAL:")
    print("  Multiplica cada dígito por 2^posición")
    print("  Ej: 1010₂ = 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 10₁₀")
    print("\nBINARIO → OCTAL:")
    print("  Agrupa de 3 en 3 bits desde la derecha")
    print("  Ej: 1 010₂ = 001 010₂ = 1 2₈ = 12₈")
    print("\nBINARIO → HEXADECIMAL:")
    print("  Agrupa de 4 en 4 bits desde la derecha")
    print("  Ej: 1010₂ = 1010₂ = A₁₆")
    print("-"*40)

# Modifica la función main para usar el menú
def main_con_menu():
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '6':
            print("👋 ¡Hasta luego!")
            break
            
        if opcion == '5':
            mostrar_ayuda()
            continue
            
        # Solicitar número binario
        numero_binario = input("Ingresa el número binario: ").strip()
        
        if not validar_binario(numero_binario):
            print("❌ Error: Número binario inválido")
            continue
            
        decimal = int(numero_binario, 2)
        
        if opcion == '1':
            print(f"\n{numero_binario}₂ = {decimal}₁₀")
        elif opcion == '2':
            octal = format(decimal, 'o')
            print(f"\n{numero_binario}₂ = {octal}₈")
        elif opcion == '3':
            hexa = format(decimal, 'X')
            print(f"\n{numero_binario}₂ = {hexa}₁₆")
        elif opcion == '4':
            octal = format(decimal, 'o')
            hexa = format(decimal, 'X')
            mostrar_resultados(numero_binario, decimal, octal, hexa)
        else:
            print("❌ Opción no válida")

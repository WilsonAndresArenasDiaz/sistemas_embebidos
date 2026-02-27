# Laboratorio de Sistemas Embebidos

## Laboratorio N° 1: Convertidor de Binario, Decimal, Octas y Hexagecimal usando PIC16F887.

### 1. Introducción
En el presente laboratorio se desarrolló un sistema embebido basado en el microcontrolador PIC16F887, cuyo objetivo es convertir un número binario de 4 bits (D, C, B, A) a sus equivalentes en sistema decimal, octal y hexadecimal.

El sistema permite visualizar el resultado decimal mediante dos displays de 7 segmentos, implementando un decodificador digital por software.

Debido a que se utilizan 4 bits de entrada, el sistema puede representar 16 combinaciones posibles, lo que establece un rango de operación entre 0 y 15.

### 2. Objetivo General

Desarrollar un sistema conversor binario utilizando el PIC16F887.


### 3. Objetivos Específicos

Diseñar el circuito electrónico.

Implementar lectura digital de 4 bits.

Programar el microcontrolador en C++.

Implementar un decodificador de 7 segmentos.

Explicar el proceso matemático de conversión.

### 3. Diseño del Circuito

#### Alimentación
VDD → +5V

VSS → GND

Resistencia 10kΩ en MCLR

Capacitor 100nF de desacoplo

#### Entradas Binarias

#### Displays 7 Segmentos

### 4. Proceso de Conversión

#### Binario → Decimal
La conversión de binario a decimal se realiza sumando las potencias de 2 correspondientes a cada bit activo. Sin embargo, en los microcontroladores, el valor leído desde un puerto digital ya es interpretado internamente como un número entero, por lo que no es necesario implementar manualmente la fórmula matemática.

#### Binario → Octal
El sistema octal trabaja en base 8. La conversión desde decimal se realiza dividiendo el número entre 8 y obteniendo el cociente y el residuo.
Por ejemplo, el número 15 en decimal equivale a 17 en octal.

#### Conversión a Hexadecimal
El sistema hexadecimal trabaja en base 16. Utiliza los símbolos del 0 al 9 y las letras A, B, C, D, E y F para representar valores entre 10 y 15.

Por ejemplo:

10 = A
11 = B
12 = C
13 = D
14 = E
15 = F

### 5. Codigo implementado

### 6. Desarrollo del Sistema

El funcionamiento del sistema se realiza en las siguientes etapas:

El usuario configura una combinación binaria mediante los interruptores.

El microcontrolador lee los 4 bits desde el puerto A.

El valor es interpretado automáticamente como un número decimal.

Se separa el número en decenas y unidades mediante operaciones de división y módulo.

Se consulta una tabla de decodificación que indica qué segmentos deben encenderse.

Los displays muestran el valor decimal correspondiente.

### 7. Tabla de Conversión

| Binario | Decimal | Octal | Hexadecimal |
| ------- | ------- | ----- | ----------- |
| 0000    | 0       | 0     | 0           |
| 0001    | 1       | 1     | 1           |
| 0010    | 2       | 2     | 2           |
| 0011    | 3       | 3     | 3           |
| 0100    | 4       | 4     | 4           |
| 0101    | 5       | 5     | 5           |
| 0110    | 6       | 6     | 6           |
| 0111    | 7       | 7     | 7           |
| 1000    | 8       | 10    | 8           |
| 1001    | 9       | 11    | 9           |
| 1010    | 10      | 12    | A           |
| 1011    | 11      | 13    | B           |
| 1100    | 12      | 14    | C           |
| 1101    | 13      | 15    | D           |
| 1110    | 14      | 16    | E           |
| 1111    | 15      | 17    | F           |

### 8. Resultados

El sistema funcionó correctamente dentro del rango esperado (0 a 15), mostrando en los displays el valor decimal correspondiente a la combinación binaria ingresada.

Las conversiones a sistema octal y hexadecimal fueron verificadas mediante cálculos teóricos y comparación con la tabla de resultados.

### 9. Conclusiones

El microcontrolador interpreta naturalmente valores binarios como números enteros.

La separación en decenas y unidades permite visualizar números de dos cifras.

El uso de una tabla de decodificación simplifica el control de los displays.

Se logró integrar correctamente hardware y software en un sistema embebido funcional.

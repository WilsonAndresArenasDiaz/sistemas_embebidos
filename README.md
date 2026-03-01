# Laboratorio de Sistemas Embebidos

<img width="1221" height="694" alt="Captura de pantalla 2026-02-27 115601" src="https://github.com/user-attachments/assets/49725986-ba31-4520-9f4a-68ef82907616" />


## Laboratorio N° 1: Convertidor de Binario, Decimal, Octas y Hexagecimal usando PIC16F887.

### 1. Introducción
En el presente laboratorio se desarrolló un sistema embebido basado en el microcontrolador PIC16F887, cuyo objetivo es convertir un número binario de 4 bits (D, C, B, A) a sus equivalentes en sistema decimal, octal y hexadecimal.

El sistema permite visualizar el resultado decimal mediante dos displays de 7 segmentos, implementando un decodificador digital por software.

Debido a que se utilizan 4 bits de entrada, el sistema puede representar 16 combinaciones posibles, lo que establece un rango de operación entre 0 y 15.

### 2. Objetivo General

Desarrollar un sistema conversor binario utilizando el PIC16F887.


### 3. Objetivos Específicos

* Diseñar el circuito electrónico.

* Implementar lectura digital de 4 bits.

* Programar el microcontrolador en C++.

* Implementar un decodificador de 7 segmentos.

### 3. Diseño del Circuito

#### Alimentación

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

#### Tabla de Conversión

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

### 5. Codigo implementado

```c
#include <xc.h>
#define _XTAL_FREQ 8000000

void UART_Init(){
    SPBRG=51;
    BRGH=1;
    SYNC=0;
    SPEN=1;
    TXEN=1;
    CREN=1;
}

void UART_Write(char data){
    while(!TRMT);
    TXREG=data;
}

void UART_Text(const char *text){
    while(*text) UART_Write(*text++);
}

char UART_Read(){
    while(!RCIF);
    return RCREG;
}

unsigned int convertirDecimal(char *valor, int base){
    unsigned int resultado=0;
    while(*valor){
        resultado*=base;
        if(*valor>='0' && *valor<='9')
            resultado+=*valor-'0';
        else if(*valor>='A' && *valor<='F')
            resultado+=*valor-'A'+10;
        valor++;
    }
    return resultado;
}

void main(){
    TRISC6=0;
    TRISC7=1;
    UART_Init();

    char valor[5];
    unsigned int decimal;
    int i;

    while(1){
        UART_Text("\r\nIngrese BIN (max4): ");
        
        for(i=0;i<4;i++){
            valor[i]=UART_Read();
            UART_Write(valor[i]);

            if(valor[i]!='0' && valor[i]!='1'){
                UART_Text("\r\nError caracter");
                break;
            }
        }

        valor[4]='\0';
        decimal=convertirDecimal(valor,2);

        if(decimal>15){
            UART_Text("\r\nError rango >15");
        }else{
            UART_Text("\r\nDecimal valido");
        }
    }
} ´´´


### 6. Desarrollo del Sistema

1. El funcionamiento del sistema se realiza en las siguientes etapas:

2. El usuario configura una combinación binaria mediante los interruptores.

3. El microcontrolador lee los 4 bits desde el puerto A.

4. El valor es interpretado automáticamente como un número decimal.

5. Se separa el número en decenas y unidades mediante operaciones de división y módulo.

6. Se consulta una tabla de decodificación que indica qué segmentos deben encenderse.

7. Los displays muestran el valor decimal correspondiente.

### 8. Resultados

El sistema funcionó correctamente dentro del rango esperado (0 a 15), mostrando en los displays el valor decimal correspondiente a la combinación binaria ingresada.

Las conversiones a sistema octal y hexadecimal fueron verificadas mediante cálculos teóricos y comparación con la tabla de resultados.



## Laboratorio N° 2: Monitoreo de ilumacion de tempratura mediante ChatBoot

### 1. Introduccion
En esta segunda etapa del laboratorio se desarrolló un sistema embebido basado en Arduino, capaz de:
* Controlar dispositivos de salida (LED rojo y verde).
* Medir variables ambientales:
    * Temperatura.
    * Humedad.
    * Nivel de iluminación.
*Recibir comandos externos mediante comunicación serial.
* Integrarse posteriormente con un chatbot con reconocimiento de voz.

El sistema implementa una arquitectura de comunicación PC ↔ Arduino mediante puerto serial, permitiendo el control y monitoreo en tiempo real.

### 2. Objivo General
Diseñar e implementar un sistema de monitoreo y control utilizando Arduino, sensores ambientales y comunicación serial.

### 4. Objetivos especificos
* Implementar lectura digital del sensor DHT11.
* Implementar lectura analógica del sensor LDR.
* Desarrollar control digital de LEDs.
* Establecer comunicación serial bidireccional.
* Permitir interpretación de comandos en lenguaje natural.

### 5. Diseño del sistema



### 6. Código
#### Arduiono

``` #include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

const int ledRojo = 8;
const int ledVerde = 9;
const int pinLDR = A1;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);

  dht.begin();

  Serial.println("Sistema listo");
}

void loop() {

  if (Serial.available()) {

    String comando = Serial.readStringUntil('\n');
    comando.trim();
    comando.toLowerCase();

    Serial.println("Recibido: " + comando);

    // ---- CONTROL LED ROJO ----
    if (comando.indexOf("rojo") != -1 && comando.indexOf("enci") != -1) {
      digitalWrite(ledRojo, HIGH);
      Serial.println("LED rojo encendido");
    }

    else if (comando.indexOf("rojo") != -1 && comando.indexOf("apag") != -1) {
      digitalWrite(ledRojo, LOW);
      Serial.println("LED rojo apagado");
    }

    // ---- CONTROL LED VERDE ----
    else if (comando.indexOf("verde") != -1 && comando.indexOf("enci") != -1) {
      digitalWrite(ledVerde, HIGH);
      Serial.println("LED verde encendido");
    }

    else if (comando.indexOf("verde") != -1 && comando.indexOf("apag") != -1) {
      digitalWrite(ledVerde, LOW);
      Serial.println("LED verde apagado");
    }

    // ---- TEMPERATURA ----
    else if (comando.indexOf("temperatura") != -1) {

      float temperatura = dht.readTemperature();

      if (isnan(temperatura)) {
        Serial.println("Error leyendo temperatura");
      } else {
        Serial.print("Temperatura actual: ");
        Serial.print(temperatura);
        Serial.println(" grados Celsius");
      }
    }

    // ---- HUMEDAD ----
    else if (comando.indexOf("humedad") != -1) {

      float humedad = dht.readHumidity();

      if (isnan(humedad)) {
        Serial.println("Error leyendo humedad");
      } else {
        Serial.print("Humedad actual: ");
        Serial.print(humedad);
        Serial.println(" %");
      }
    }

    // ---- LUZ ----
    else if (comando.indexOf("luz") != -1) {

      int valorLuz = analogRead(pinLDR);

      Serial.print("Nivel de luz: ");
      Serial.println(valorLuz);
    }

    else {
      Serial.println("Comando no reconocido");
    }
  }
} ```

#### Chatbot con Voz




### .7 Funcionamiento del Sistema
El sistema opera bajo un esquema de recepción de comandos:
1. El Arduino espera datos en el puerto serial.
2. Recibe una cadena de texto.
3. Convierte el texto a minúsculas.
4. Busca palabras clave.
5. Ejecuta la acción correspondiente.

Ejemplos de comandos:
* "enciende el rojo"
* "apaga el verde"
* "dime la temperatura"
* "dime la humedad"
* "dime el nivel de luz"

*Video*: 






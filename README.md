# Laboratorio de Sistemas Embebidos

## Laboratorio N° 1: Convertidor de Binario, Decimal, Octas y Hexagecimal usando PIC16F887.

<img width="1221" height="694" alt="Captura de pantalla 2026-02-27 115601" src="https://github.com/user-attachments/assets/49725986-ba31-4520-9f4a-68ef82907616" />


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

### 4. Codigo implementado

```
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
}
```


### 5. Funcionamiento del Sistema

1. El funcionamiento del sistema se realiza en las siguientes etapas:

2. El usuario configura una combinación binaria mediante los interruptores.

3. El microcontrolador lee los 4 bits desde el puerto A.

4. El valor es interpretado automáticamente como un número decimal.

5. Se separa el número en decenas y unidades mediante operaciones de división y módulo.

6. Se consulta una tabla de decodificación que indica qué segmentos deben encenderse.

7. Los displays muestran el valor decimal correspondiente.

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






## Laboratorio N° 2: Monitoreo de ilumacion de tempratura mediante ChatBoot

<img width="1274" height="701" alt="Captura de pantalla 2026-03-01 120220" src="https://github.com/user-attachments/assets/3aca48d3-1000-4fd5-9190-11314f220c82" />


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

### 3. Objetivos especificos
* Implementar lectura digital del sensor DHT11.
* Implementar lectura analógica del sensor LDR.
* Desarrollar control digital de LEDs.
* Establecer comunicación serial bidireccional.
* Permitir interpretación de comandos en lenguaje natural.

### 4. Diseño del sistema

![Multimedia](https://github.com/user-attachments/assets/4e0eae4d-9d29-4193-ae23-2ebf0f28d64e)


El sistema se compone de sensores de entrada, actuadores de salida y comunicación serial con el computador.

#### Conexión del DHT11 (Temperatura y Humedad)
* VCC → 5V del Arduino
* GND → GND del Arduino
* DATA → Pin digital 2
El sensor envía datos digitales, por lo que no usa entrada analógica.

#### Conexión del LDR (Iluminación)
* Una terminal del LDR → 5V
* La otra terminal → Pin A1
* Desde A1 → Resistencia 10kΩ → GND
Esto permite que el Arduino mida la variación de luz mediante el ADC (0–1023).

#### Conexión del LED Rojo
* Pin 8 → Resistencia 220Ω → Ánodo del LED
* Cátodo → GND

#### Conexión del LED Verde
* Pin 9 → Resistencia 220Ω → Ánodo del LED
* Cátodo → GND

#### Comunicación
Se utiliza comunicación serial USB a 9600 baudios para enviar comandos y recibir respuestas desde el computador.


### 5. Código

#### Arduiono

```
#include <DHT.h>

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
}
```

#### Chatbot con Voz

```
import streamlit as st
from gtts import gTTS
import serial
import time
import base64
from streamlit_mic_recorder import speech_to_text

# CONFIGURA TU PUERTO
PUERTO = "COM5"  # Cambia por tu puerto
BAUDIOS = 9600

arduino = serial.Serial(PUERTO, BAUDIOS)
time.sleep(2)

st.title("Chatbot con Voz + Arduino")

texto = speech_to_text(language="es", use_container_width=True, just_once=True)

if texto:
    st.write("Tú:", texto)

    # Enviar comando al Arduino
    arduino.write((texto + "\n").encode())
    time.sleep(1)

    respuesta = ""

    while arduino.in_waiting:
        respuesta = arduino.readline().decode().strip()

    st.write("Arduino:", respuesta)

    # Convertir respuesta a voz
    tts = gTTS(respuesta, lang="es")
    tts.save("respuesta.mp3")

    audio_file = open("respuesta.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

    audio_file.close()
```


### 6. Funcionamiento del Sistema
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

#### Video: https://unipanamericanaeduco-my.sharepoint.com/:v:/g/personal/afgarciadelrio_ucompensar_edu_co/IQC0cIhxw5J2Qr4rnXT7m7iVATZeNg57dsTgvA5ygQulGAE?e=H1RfdB






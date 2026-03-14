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

### 4. Diseño del Circuito

El sistema se implementa utilizando el microcontrolador PIC16F887, un módulo HEX Keypad y dos displays de 7 segmentos.

El interruptor DIP permite ingresar un número en formato binario de 4 bits (A, B, C, D), el cual es leído por el microcontrolador a través de cuatro pines de entrada. Este valor binario puede representar números entre 0 y 15.

El microcontrolador procesa este valor y lo convierte a su equivalente en dos dígitos decimales, los cuales se muestran en los dos displays de 7 segmentos:

* Display 1: muestra la decena

* Display 2: muestra la unidad

Por ejemplo, si el valor binario corresponde al número 15, el primer display mostrará 1 y el segundo display mostrará 5.

#### Conexiones del sistema

| Componente               | Conexión al PIC |
| ------------------------ | --------------- |
| HEX Keypad D0            | RA0             |
| HEX Keypad D1            | RA1             |
| HEX Keypad D2            | RA2             |
| HEX Keypad D3            | RA3             |
| Segmento A               | RB0             |
| Segmento B               | RB1             |
| Segmento C               | RB2             |
| Segmento D               | RB3             |
| Segmento E               | RB4             |
| Segmento F               | RB5             |
| Segmento G               | RB6             |
| Control display decenas  | RC0             |
| Control display unidades | RC1             |

Cada segmento del display se conecta mediante resistencias de 220Ω para proteger los LEDs del display.

Los dos displays son controlados mediante multiplexación, activando cada uno de forma alternada para mostrar los dos dígitos del número.

### 5. Codigo implementado

```
#include <16F887.h>
#fuses HS,NOWDT,NOLVP
#use delay(clock=20000000)

const int tabla7seg[10] = {
   0b00111111, //0
   0b00000110, //1
   0b01011011, //2
   0b01001111, //3
   0b01100110, //4
   0b01101101, //5
   0b01111101, //6
   0b00000111, //7
   0b01111111, //8
   0b01101111  //9
};

void main(){

   int valor;
   int decenas;
   int unidades;

   set_tris_a(0x0F);
   set_tris_b(0x00);
   set_tris_c(0x00);

   while(TRUE){

      valor = input_a() & 0x0F;

      decenas = valor / 10;
      unidades = valor % 10;

      // Mostrar decenas
      output_high(PIN_C0);
      output_low(PIN_C1);
      output_b(tabla7seg[decenas]);
      delay_ms(5);

      // Mostrar unidades
      output_low(PIN_C0);
      output_high(PIN_C1);
      output_b(tabla7seg[unidades]);
      delay_ms(5);
   }
}
```

Se realiza homologacion a un arduino por fallas en el programador de pic 

Se monta en arduino con pantalla led 16x2 con i2c donde muestra el bin y una conversion a cada sistema, el diseño es un arduino alimentado por puerto serial de ahy en los pines 

A4 a SDA

A5 a scl

5v a vcc

gnd a gnd 


A2 a A dip

A3 a B dip 

A4 a C dip 

A5 a d dip 

los demas del dip a tierra 


### 6. Funcionamiento del Sistema

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


### 5. Código implementado

#### Arduino

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




## Laboratorio N° 3: 

### 1. Introduccion

En este laboratorio se desarrolló un sistema de monitoreo y control que integra sensores, microcontroladores y visión artificial. El sistema utiliza OpenCV en Python para detectar objetos mediante la cámara del computador.
La información detectada se envía por comunicación serial hacia Arduino Uno, el cual permite controlar dispositivos electrónicos del sistema.

### 2. Objivo General
Diseñar e implementar un sistema de monitoreo y control utilizando Arduino, sensores ambientales y comunicación serial.

### 3. Objetivos especificos

* Implementar la lectura de sensores mediante Arduino.

* Desarrollar un sistema de detección de objetos usando visión artificial.

* Establecer comunicación serial entre el computador y Arduino.

* Integrar el procesamiento de imágenes con el control de hardware.

### 4. Diseño del sistema

El sistema está compuesto por tres elementos principales: el computador, el Arduino Uno y el microcontrolador PIC16F887.

El computador ejecuta el programa desarrollado en Python utilizando la librería OpenCV, el cual permite capturar imágenes mediante la cámara y detectar objetos según su color o forma.

Una vez identificado el objeto, el programa envía un comando a través del puerto serial hacia el Arduino. El Arduino actúa como puente de comunicación y retransmite el mensaje hacia el PIC16F887.

El PIC recibe la información mediante comunicación serial y activa los LEDs correspondientes según el objeto detectado.

#### Conexiones del sistema

##### Arduino – Computador

La conexión se realiza mediante cable USB, permitiendo la comunicación serial entre Python y Arduino.

##### Arduino	PIC16F887

| Arduino    | PIC16F887 | Descripción                               |
| ---------- | --------- | ----------------------------------------- |
| TX (Pin 1) | RC7 (RX)  | Transmisión de datos desde Arduino al PIC |
| GND        | GND       | Referencia de tierra compartida           |


##### LEDs conectados al PIC

| Dispositivo | Pin PIC16F887 | Descripción                     |
| ----------- | ------------- | ------------------------------- |
| LED rojo    | RB0           | Indica detección de objeto rojo |
| LED azul    | RB1           | Indica detección de objeto azul |
| LED verde   | RB2           | Indicador adicional del sistema |

Cada LED se conecta en serie con una resistencia de 220Ω hacia tierra (GND).


### 5. Código implementado

#### Código Python (OpenCV)

```
import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('COM3',9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

red_lower = np.array([0,100,100])
red_upper = np.array([10,255,255])

blue_lower = np.array([100,100,100])
blue_upper = np.array([130,255,255])

while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red = cv2.inRange(hsv, red_lower, red_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    contours_red,_ = cv2.findContours(mask_red,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours_blue,_ = cv2.findContours(mask_blue,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours_red:
        if cv2.contourArea(cnt) > 500:
            arduino.write(b"R")

    for cnt in contours_blue:
        if cv2.contourArea(cnt) > 500:
            arduino.write(b"A")

    cv2.imshow("Camara",frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

##### Código Arduino

```
void setup() {

  Serial.begin(9600);

}

void loop() {

  if(Serial.available()){

    char dato = Serial.read();

    Serial.write(dato);

  }

}
```

#### Código PIC16F887

```
#include <16F887.h>
#fuses HS,NOWDT,NOLVP
#use delay(clock=20000000)

#use rs232(baud=9600,xmit=PIN_C6,rcv=PIN_C7)

void main(){

   char dato;

   set_tris_b(0x00);

   while(TRUE){

      if(kbhit()){

         dato = getc();

         if(dato == 'R'){
            output_high(PIN_B0);
         }

         if(dato == 'A'){
            output_high(PIN_B1);
         }

      }

   }

}
```


### 6. Funcionamiento del Sistema

El sistema inicia activando la cámara del computador y ejecutando el programa de procesamiento de imágenes.
Cuando se detecta un objeto con las características definidas, el sistema envía un comando al Arduino.
El Arduino procesa la información y activa el dispositivo correspondiente, permitiendo realizar acciones de control basadas en la detección visual.



#### Video:







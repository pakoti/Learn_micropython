# Learn_micropython
Learn micropython on ESP32,ESP8266




## Getting Started With MicroPython on the ESP8266

What Is MicroPython ?

Requirements

Setting Up Your Computer

Install device drivers

If you have a Linux computer, then you do not need to install any device drivers for the drivers for the microcontroller to be recognized.But it you have a Mac or a Windows machine, a driver is needed to allow the computer to recognized the microcontroller as a serial device.


Install Python

The tools that you are going to use to communicate with the ESP8266 are written in Python, so you need to install Python on your computer.

If your operating system does not provide a pre-packaged Python, you can go to https://python.org to download an official build for any of the supported operating systems.


Install esptool and rshell

Install two packages that are going to help you manage your board using pip.To do this open your terminal and run

    pip install esptool rshell


Download MicroPython

Download the latest MicroPython firmware .bin from the following link: https://micropython.org/download#esp8266



Flashing MicroPython With Esptool.py


Before flashing a new firmware into the board it is a good idea to erase any previous data.This is something that you should always do so that the new firmware runs from a clean state.Go where you have placed the .bin file. Use esptool.py to erase the flash.

For Linux:

    esptool.py --port /dev/ttyUSB0 erase_flash


For Windows:

    esptool.py --port COM3 erase_flash



You may have to change the serial port in your command to the serial port that your ESP8266 board is connected to. If you do not know the serial port number of your ESP8266, you can check in the Arduino IDE. Just open the IDE and then click on Tools | Ports. You should see the serial port of your ESP8266 board listed there. Replace the serial port in the command (/dev/ttyUSB0 ) with the serial port of your board.

Now that the board is completely erased, you can flash the MicroPython build that you just downloaded.This is also done with the esptool.py command:

esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash 0 esp8266-20190529-v1.11.bin
This command is going to write the contents of the MicroPython .bin file to the board at address 0.

Make sure you change the name of the firmware .bin file in the command ( esp82688-2019-080529-v1.11.bin) to that of the firmware you downloaded.

Once the firmware is successfully installed on your ESP8266 board, you can access REPL on your board via a wired connection ( UART serial port) or thought WiFi.


Step 6: Using the MicroPython REPL With Rshell


You are now ready to start MicroPython on your ESP8266 board.

What I'm going to show you how to connect to the Python prompt running on your board.This is called the REPL, which stands for "Read-Eval-Print-Loop". This is the standard Python prompt that you are probably used to see when working with the regular Python interpreter, but this time it is going to be running on your board, and to interact with it you are going to use the serial connection to your computer. Ready?

To connect to your board and open a REPL session, enter the following command:

    rshell --port <your board port name>

This command will bring you into the rshell prompt. See photo above.

If you are following this tutorial on Windows, note that rshell has a history of problems when running on Windows.

So in order to fix that type:

    rshell -a --port COM3

From this prompt you can perform management tasks related to your
microcontroller board, and also start a Python REPL that you can use to interact with the board in real time.So just entering the following command:

    repl

To make sure everything is working, type a simple Python sentence:

print("Hello World")
# Smart Drink Dispenser
Smart Drink Dispenser project for Embedded Systems Class. This is an ECE 4180 project by  Michael Chan, Ransom Conant, Pratik Kunapuli, and Vineet Nadella

[Video](https://drive.google.com/file/d/1h0J8PITRjtYM9t8H9RYf7_4x0Liw44gI/view)

## Project Description

This project is a smart bartender using a raspberry pi and DC peristaltic pumps to mix any drink you want. There is a touchscreen LCD used to control the device, and pre-defined mixed drinks are available to select. Once selected, the device will begin to pour the drink.

[Device](Images/Device_Picture.png)

## Hardware Needed
- Raspberry Pi 3
- Parastaltic Pumps (6)
- MOSFET Breakout Boards (6) [Link](https://www.sparkfun.com/products/12959)
- AC-DC Converter
- DC Voltage Regulator
- LCD Touchscreen

## Electrical Schematic
Example electrical schematic:
[Schmatic](Images/Electrical_Schematic.png)

[Electronics](Images/Electronics.png)

## Hardware 
Wood paneling was used to enclose the device, creating a box that contains a spot for a cup to be placed underneath the funnel. The 6 pumps are mounted on the back of the device, so that the drinks can be outside of the device, with plenty of tubing going from the pump to the drink. The other side of the pump's tubing is routed through the top of the device and leads into the aformentioned funnel, above the empty  cup. Underneath the platform where the cup sits, all of the electronics are mounted in a hidden compartment. The AC-DC converted, breadboard, voltage regulator, Raspberry Pi and MOSFET breakout boards are all contained within this space.

## Code
The code is entirely contained within the `bartender.py` file. Future work includes adding Amazon Alexa support to be able to request a drink via voice from anywhere. A picture of the GUI is shown below.

[GUI](Images/GUI.png)

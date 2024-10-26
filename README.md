# devlab-interface

This is a simple middleware that connects our system with the laboratory machines.

<u>Objective:</u> Create a middleware that can interpret the data then provide the machine and decode and convert in a format that is easy to integrate into our backend system.

This interface contemplates the communication protocol HL7 (Health Level Seven) and data exporting with RS232 or TCP/IP.

1.- Libraries to serial communication:
 * pySerial
 * Request

2.- Basic configuration to read data from the serial port

3.- Read and process the data of the device

4.- Send data to backend

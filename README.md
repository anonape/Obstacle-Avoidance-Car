# Wireless Remote Car - using Raspberry Pi 3 and Arduino

We implemented a wireless moving wooden vehicle. We carved wheels and a body in using the Georgia Tech wood cutting inventure studio. We then mounted a raspberry Pi, Arduino, and breadboard (with a H-Bridge) on the platform of the wooden vehicle. We used the Arduino and a ultrasonic sensor to control the front-wheel motors on the wheels. Then, we setup a wireless server on the raspberry pi 3 and took input from our computers. Therefore, we setup a client-server model using the raspberry pi 3 over a wireless network hosted by the Rpi 3 and the RPi 3 sent commands to the Arduino via USB to control the motors. The sensors were used to automatically steer the car away, without the need for the user to avoid an obstacle.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

-Pyro4
-Arduino IDE
-Connect and setup raspberry pi 3 environment


### Deploying server and setting up client

A step by step series of examples that tell you have to get a development env running

Say what the step will be

-python greeting-server.py on raspberry pi 3 acting as server
-python greeting-clinet.py on client computer sending instructions


## Authors
-Shivam Patel
-Akhila Ballari
-Raghav Mittal
-Varun Ballari
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

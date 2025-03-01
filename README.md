# Thermostat

A thermostat application written in Python, designed to run on a Raspberry Pi Zero W.

The application uses a [DS18B20 temperature sensor](https://www.adafruit.com/product/374) and a [30 amp 120V relay](https://www.amazon.com/gp/product/B07XKQTV9G) connected to the Raspberry Pi.

The application uses [MQTT](https://mqtt.org/) to transmit statistics and receive temperature changes.

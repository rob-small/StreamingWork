A set of data generator generator program for generating, interacting with, and capturing streaming data.

Allows the creation of a set of sensor devices that provide a reading upon request based on the normal distribution around a set value.

mydevice.py - Base class that represent a sensor device
app.py - Flask microservice that creates a range of sensor devices and allows for interaction with them.
data.json - Initial configuration of sensors used at start of application
config.json - Configuration for application end points
client.py - Takes periodic readings from devices
client-device-setup.py - Creates initial device configurations

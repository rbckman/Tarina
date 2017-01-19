import smbus
import time

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(3) # Rev 2 Pi uses 1

DEVICE = 0x20 # Device address (A0-A2)
IODIRB = 0x0d # Pin direction register
GPIOB  = 0x13 # Register for inputs

bus.write_byte_data(DEVICE,IODIRB,0xFF) # set all gpiob to input

# Loop until user presses CTRL-C
while True:
    # Read state of GPIOA register
    readbus = bus.read_byte_data(DEVICE,GPIOB)
    print readbus
    time.sleep(0.1)
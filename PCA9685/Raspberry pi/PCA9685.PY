import smbus
import time

bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards
address = 0x40  # The I2C address of the PCA9685

def set_pwm(channel, on_time, off_time):
    register = 4 * channel
    bus.write_byte_data(address, register + 0, on_time & 0xFF)
    bus.write_byte_data(address, register + 1, on_time >> 8)
    bus.write_byte_data(address, register + 2, off_time & 0xFF)
    bus.write_byte_data(address, register + 3, off_time >> 8)

# Set the frequency of PWM signals (default is 200Hz)
def set_pwm_frequency(frequency):
    prescale_value = 25000000.0  # 25MHz
    prescale_value /= 4096.0  # 12-bit resolution
    prescale_value /= float(frequency)
    prescale_value -= 1.0
    prescale = int(prescale_value + 0.5)
    
    old_mode = bus.read_byte_data(address, 0x00)
    new_mode = (old_mode & 0x7F) | 0x10  # Sleep mode
    bus.write_byte_data(address, 0x00, new_mode)  # Go to sleep
    bus.write_byte_data(address, 0xFE, prescale)  # Set the prescaler
    bus.write_byte_data(address, 0x00, old_mode)  # Wake up

# Example usage:
set_pwm_frequency(100)  # Set the PWM frequency to 100Hz

# Set the pulse width for channel 0 (values between 0 and 4095)
set_pwm(0, 0, 2048)  # ON time: 0, OFF time: 2048 (50% duty cycle)
time.sleep(1)  # Wait for 1 second

set_pwm(0, 0, 4095)  # ON time: 0, OFF time: 4095 (100% duty cycle)
time.sleep(1)  # Wait for 1 second

set_pwm(0, 2048, 4095)  # ON time: 2048, OFF time: 4095 (75% duty cycle)
time.sleep(1)  # Wait for 1 second

# You can control other channels in a similar way

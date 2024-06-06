import time
import pigpio

class DHT22:
    def __init__(self, pi, gpio):
        self.pi = pi
        self.gpio = gpio
        self.data = []
        self._cb = None

    def read(self):
        self.pi.set_mode(self.gpio, pigpio.OUTPUT)
        self.pi.write(self.gpio, pigpio.LOW)
        time.sleep(0.018)
        self.pi.set_mode(self.gpio, pigpio.INPUT)
        
        self.data = []
        self._cb = self.pi.callback(self.gpio, pigpio.EITHER_EDGE, self._cbf)

        time.sleep(0.2)
        self._cb.cancel()
        data = self.data

        if len(data) != 84:
            return None, None

        bits = []
        for i in range(2, len(data) - 1, 2):
            bits.append(data[i+1] - data[i])

        humidity = 0
        temperature = 0

        for i in range(16):
            humidity += bits[i] << (15 - i)
            temperature += bits[16 + i] << (15 - i)

        return humidity / 10.0, temperature / 10.0

    def _cbf(self, gpio, level, tick):
        self.data.append(tick)

pi = pigpio.pi()
dht22 = DHT22(pi, 4)  # GPIO 4번 핀 사용

while True:
    humidity, temperature = dht22.read()
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.2f}C  Humidity: {humidity:.2f}%")
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(1)

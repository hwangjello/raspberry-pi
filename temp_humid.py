import Adafruit_DHT
import time

# DHT 센서 설정
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # 데이터 핀 연결 GPIO 핀 번호 (예: GPIO4)

while True:
    # 온도와 습도 읽기
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    # 읽기 성공 여부 확인
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.2f}C  Humidity: {humidity:.2f}%")
    else:
        print("Failed to retrieve data from humidity sensor")
    
    # 1초 대기
    time.sleep(1)

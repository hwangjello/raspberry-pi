import time
import board
import adafruit_dht

# DHT22 센서 설정
dht_device = adafruit_dht.DHT22(board.D4)  # D4 핀 사용, 실제 연결된 핀으로 변경

while True:
    try:
        # 온도와 습도 읽기
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        
        # 읽기 성공 여부 확인
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.2f}C  Humidity: {humidity:.2f}%")
        else:
            print("Failed to retrieve data from humidity sensor")
    
    except RuntimeError as error:
        # 읽기 오류 발생 시
        print(f"Error reading from DHT22: {error.args[0]}")
    
    time.sleep(1)

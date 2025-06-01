import json
from collections import defaultdict

def read_weather_data(filename='weather_data.json'):
    """Đọc dữ liệu thời tiết từ file JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data['weather_data']
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Lỗi định dạng JSON trong file {filename}")
        return []

def analyze_weather_data(weather_data):
    """Phân tích dữ liệu thời tiết"""
    # Thống kê theo thành phố
    city_stats = {}
    for entry in weather_data:
        city = entry['city']
        if city not in city_stats:
            city_stats[city] = {
                'total_temp': 0,
                'total_humidity': 0,
                'total_rainfall': 0,
                'count': 0
            }
        
        city_stats[city]['total_temp'] += entry['temperature']
        city_stats[city]['total_humidity'] += entry['humidity']
        city_stats[city]['total_rainfall'] += entry['rainfall']
        city_stats[city]['count'] += 1

    # In thống kê
    print("\nThống kê thời tiết:")
    for city, stats in city_stats.items():
        print(f"\nThành phố: {city}")
        print(f"Nhiệt độ trung bình: {stats['total_temp'] / stats['count']:.1f}°C")
        print(f"Độ ẩm trung bình: {stats['total_humidity'] / stats['count']:.1f}%")
        print(f"Tổng lượng mưa: {stats['total_rainfall']} mm")

def calculate_average_temperature(weather_data):
    """Tính nhiệt độ trung bình của mỗi thành phố"""
    city_temps = defaultdict(list)
    
    for entry in weather_data:
        city_temps[entry['city']].append(entry['temperature'])
    
    print("\nNhiệt độ trung bình của mỗi thành phố:")
    for city, temps in city_temps.items():
        avg_temp = sum(temps) / len(temps)
        print(f"{city}: {avg_temp:.1f}°C")

def find_highest_rainfall_day(weather_data):
    """Tìm ngày có lượng mưa cao nhất"""
    max_rainfall_day = max(weather_data, key=lambda x: x['rainfall'])
    
    print("\nNgày có lượng mưa cao nhất:")
    print(f"Ngày: {max_rainfall_day['date']}")
    print(f"Thành phố: {max_rainfall_day['city']}")
    print(f"Lượng mưa: {max_rainfall_day['rainfall']} mm")

def compare_humidity(weather_data):
    """So sánh độ ẩm trung bình giữa Hà Nội và TP.HCM"""
    city_humidity = defaultdict(list)
    
    for entry in weather_data:
        city_humidity[entry['city']].append(entry['humidity'])
    
    print("\nSo sánh độ ẩm trung bình:")
    for city, humidities in city_humidity.items():
        avg_humidity = sum(humidities) / len(humidities)
        print(f"{city}: {avg_humidity:.1f}%")
    
    # So sánh trực tiếp
    hanoi_humidity = sum(city_humidity['Hà Nội']) / len(city_humidity['Hà Nội'])
    hcm_humidity = sum(city_humidity['TP.HCM']) / len(city_humidity['TP.HCM'])
    
    print("\nSự khác biệt độ ẩm:")
    if hanoi_humidity > hcm_humidity:
        print(f"Hà Nội có độ ẩm cao hơn TP.HCM {hanoi_humidity - hcm_humidity:.1f}%")
    else:
        print(f"TP.HCM có độ ẩm cao hơn Hà Nội {hcm_humidity - hanoi_humidity:.1f}%")

def main():
    # Đọc dữ liệu từ file
    weather_data = read_weather_data()
    
    # In toàn bộ dữ liệu
    print("Chi tiết dữ liệu thời tiết:")
    for entry in weather_data:
        print(f"Ngày: {entry['date']}, Thành phố: {entry['city']}, "
              f"Nhiệt độ: {entry['temperature']}°C, "
              f"Độ ẩm: {entry['humidity']}%, "
              f"Lượng mưa: {entry['rainfall']} mm")
    
    # Phân tích dữ liệu
    analyze_weather_data(weather_data)
    
    # Tính nhiệt độ trung bình
    calculate_average_temperature(weather_data)
    
    # Tìm ngày có lượng mưa cao nhất
    find_highest_rainfall_day(weather_data)
    
    # So sánh độ ẩm
    compare_humidity(weather_data)

if __name__ == "__main__":
    main()

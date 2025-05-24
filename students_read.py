import json
import os

# Lấy đường dẫn hiện tại của file Python
current_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn đầy đủ tới file JSON
file_path = os.path.join(current_dir, 'students_data.json')

def read_students_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            students = json.load(file)
        
        # Sắp xếp sinh viên theo tên (alphabet)
        sorted_students = sorted(students, key=lambda x: x['name'])
        
        # In thông tin sinh viên đã sắp xếp
        print("Danh sách sinh viên (sắp xếp theo tên từ A-Z):")
        for student in sorted_students:
            print(f"Tên: {student['name']}")
            print(f"Lớp: {student['class']}")
            print(f"Nước: {student['country']}")
            print("---")
        
        # Các phần thống kê khác vẫn giữ nguyên
        # Thống kê số lượng nước
        unique_countries = set()
        for student in students:
            unique_countries.add(student['country'])
        
        print(f"\nTổng số nước: {len(unique_countries)}")
        print("Danh sách các nước:")
        for country in sorted(unique_countries):
            print(country)
        
        # Liệt kê sinh viên có tên chứa "m" hoặc "M"
        print("\nDanh sách sinh viên có tên chứa 'm' hoặc 'M':")
        students_with_m = [
            student for student in students 
            if 'm' in student['name'].lower()
        ]
        
        # In thông tin sinh viên có tên chứa "m" hoặc "M"
        for student in students_with_m:
            print(f"Tên: {student['name']}")
            print(f"Lớp: {student['class']}")
            print(f"Nước: {student['country']}")
            print("---")
        
        # Đếm số lượng sinh viên có tên chứa "m" hoặc "M"
        print(f"\nTổng số sinh viên có tên chứa 'm' hoặc 'M': {len(students_with_m)}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {filename}")
    except json.JSONDecodeError:
        print(f"Lỗi: File {filename} không đúng định dạng JSON")

# Chạy chương trình
read_students_data(file_path)

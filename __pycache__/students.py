import json
import os

def read_students_json(filename):
    """Đọc dữ liệu sinh viên từ file JSON"""
    # Lấy đường dẫn thư mục hiện tại
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            students_data = json.load(file)
            return students_data['students']
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Lỗi: File {file_path} không đúng định dạng JSON")
        return []

def calculate_average_grade(student):
    """Tính điểm trung bình của một học sinh"""
    grades = student['grades']
    if not grades:
        return 0
    
    # Tính điểm trung bình
    total_grade = sum(grades.values())
    average_grade = total_grade / len(grades)
    
    return round(average_grade, 2)

def find_top_student(students):
    """Tìm học sinh có điểm trung bình cao nhất"""
    if not students:
        return None
    
    # Tìm học sinh có điểm trung bình cao nhất
    top_student = max(students, key=calculate_average_grade)
    
    return top_student

def main():
    # Đọc file students_data.json
    students = read_students_json('students_data.json')
    
    # In thông tin điểm trung bình của từng học sinh
    print("Điểm trung bình của từng học sinh:")
    for student in students:
        avg_grade = calculate_average_grade(student)
        print(f"{student['name']}: {avg_grade}")
    
    # Tìm và in thông tin học sinh có điểm trung bình cao nhất
    top_student = find_top_student(students)
    
    if top_student:
        top_avg_grade = calculate_average_grade(top_student)
        print("\nHọc sinh có điểm trung bình cao nhất:")
        print(f"Tên: {top_student['name']}")
        print(f"Điểm trung bình: {top_avg_grade}")
    else:
        print("Không có học sinh nào trong danh sách.")

if __name__ == "__main__":
    main()

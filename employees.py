import json
from collections import defaultdict

def read_employees_from_file(filename='employees_data.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['employees']
    except Exception as e:
        print(f"Lỗi đọc file: {e}")
        return []

def calculate_avg_salary_by_department(employees):
    """Tính lương trung bình theo phòng ban"""
    department_salaries = defaultdict(list)
    
    for employee in employees:
        department_salaries[employee['department']].append(employee['salary'])
    
    print("\n🔹 Lương trung bình theo phòng ban:")
    for dept, salaries in department_salaries.items():
        avg_salary = sum(salaries) / len(salaries)
        print(f"{dept}: {avg_salary:,.0f} VND")

def find_most_experienced_employee(employees):
    """Tìm nhân viên có kinh nghiệm nhiều nhất"""
    most_experienced = max(employees, key=lambda x: x['experience_years'])
    
    print("\n🔹 Nhân viên có kinh nghiệm nhiều nhất:")
    print(f"Tên: {most_experienced['name']}")
    print(f"Phòng ban: {most_experienced['department']}")
    print(f"Năm kinh nghiệm: {most_experienced['experience_years']}")
    print(f"Lương: {most_experienced['salary']:,} VND")

def count_employees_by_department(employees):
    """Đếm số nhân viên trong mỗi phòng ban"""
    department_counts = defaultdict(int)
    
    for employee in employees:
        department_counts[employee['department']] += 1
    
    print("\n🔹 Số nhân viên theo phòng ban:")
    for dept, count in department_counts.items():
        print(f"{dept}: {count} nhân viên")

def main():
    # Đọc dữ liệu nhân viên
    employees = read_employees_from_file()
    
    if not employees:
        return
    
    # In thông tin chi tiết từng nhân viên
    print("🔸 Thông tin chi tiết nhân viên:")
    for employee in employees:
        print(f"ID: {employee['id']}")
        print(f"Tên: {employee['name']}")
        print(f"Phòng ban: {employee['department']}")
        print(f"Lương: {employee['salary']:,} VND")
        print(f"Năm kinh nghiệm: {employee['experience_years']}")
        print("---")
    
    # Gọi các hàm phân tích
    calculate_avg_salary_by_department(employees)
    find_most_experienced_employee(employees)
    count_employees_by_department(employees)

if __name__ == "__main__":
    main()

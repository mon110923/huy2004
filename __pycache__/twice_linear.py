import heapq

def dbl_linear(n):
    seen = set([1])
    heap = [1]
    
    for _ in range(n):
        x = heapq.heappop(heap)
        
        y = 2 * x + 1
        z = 3 * x + 1
        
        if y not in seen:
            heapq.heappush(heap, y)
            seen.add(y)
        
        if z not in seen:
            heapq.heappush(heap, z)
            seen.add(z)
    
    return heapq.heappop(heap)

# Hàm main để kiểm tra
def main():
    # Các test case
    test_cases = [10, 20, 30, 50]
    
    for case in test_cases:
        result = dbl_linear(case)
        print(f"dbl_linear({case}) = {result}")

# Kiểm tra kết quả cụ thể
def check_specific_cases():
    print("Kiểm tra các test case cụ thể:")
    print(f"dbl_linear(10) = {dbl_linear(10)}")  # Kỳ vọng: 22
    print(f"dbl_linear(20) = {dbl_linear(20)}")  # Kỳ vọng: 57
    print(f"dbl_linear(30) = {dbl_linear(30)}")  # Kỳ vọng: 91
    print(f"dbl_linear(50) = {dbl_linear(50)}")  # Kỳ vọng: 175

# Chạy chương trình
if __name__ == "__main__":
    # Chạy main
    main()
    
    # Kiểm tra các test case cụ thể
    check_specific_cases()

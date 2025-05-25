def sum_of_proper_divisors(n):
    if n < 2:
        return 0
    
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    
    return total

def buddy(start, limit):
    return next(
        ([n, m] for n in range(start, limit + 1) 
         if (m := sum_of_proper_divisors(n) - 1) > n 
         and sum_of_proper_divisors(m) == n + 1), 
        "Nothing"
    )

# Hàm main để kiểm tra
def main():
    # Các test case
    test_cases = [
        (10, 50),   # Ví dụ 1
        (1071, 1171),  # Ví dụ 2
        (2382, 2502),  # Ví dụ 3
    ]
    
    # Chạy các test case
    for start, limit in test_cases:
        result = buddy(start, limit)
        print(f"Buddy pair for range {start} to {limit}: {result}")

# Kiểm tra nếu đang chạy trực tiếp script
if __name__ == "__main__":
    main()

import json

class Product:
    def __init__(self, id, name, price, category, stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

class ProductManager:
    def __init__(self, filename='products_data.json'):
        self.filename = filename
        self.products = []
        self.load_products()

    def load_products(self):
        """
        Tải danh sách sản phẩm từ file JSON
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.products = [
                    Product(
                        p['id'], 
                        p['name'], 
                        p['price'], 
                        p['category'], 
                        p['stock']
                    ) for p in data['products']
                ]
        except FileNotFoundError:
            print(f"Không tìm thấy file {self.filename}")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")

    def save_products(self):
        """
        Lưu danh sách sản phẩm vào file JSON
        """
        try:
            data = {
                'products': [
                    {
                        'id': p.id,
                        'name': p.name,
                        'price': p.price,
                        'category': p.category,
                        'stock': p.stock
                    } for p in self.products
                ]
            }
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("Đã lưu sản phẩm thành công!")
        except Exception as e:
            print(f"Lỗi khi lưu file: {e}")

    def display_products(self):
        """
        Hiển thị toàn bộ sản phẩm
        """
        if not self.products:
            print("Không có sản phẩm nào.")
            return

        print("Danh sách sản phẩm:")
        for product in self.products:
            print(f"ID: {product.id}")
            print(f"Tên: {product.name}")
            print(f"Giá: {product.price:,} VND")
            print(f"Danh mục: {product.category}")
            print(f"Tồn kho: {product.stock}")
            print("---")

    def add_product(self, product):
        """
        Thêm sản phẩm mới
        """
        # Kiểm tra ID đã tồn tại chưa
        if any(p.id == product.id for p in self.products):
            print(f"Sản phẩm với ID {product.id} đã tồn tại.")
            return False
        
        self.products.append(product)
        self.save_products()
        return True

    def update_product(self, product_id, updated_product):
        """
        Cập nhật thông tin sản phẩm
        """
        for i, product in enumerate(self.products):
            if product.id == product_id:
                self.products[i] = updated_product
                self.save_products()
                return True
        
        print(f"Không tìm thấy sản phẩm có ID {product_id}")
        return False

    def delete_product(self, product_id):
        """
        Xóa sản phẩm theo ID
        """
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                self.save_products()
                return True
        
        print(f"Không tìm thấy sản phẩm có ID {product_id}")
        return False

    def find_product_by_id(self, product_id):
        """
        Tìm sản phẩm theo ID
        """
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def filter_products_by_category(self, category):
        """
        Lọc sản phẩm theo danh mục
        """
        return [
            product for product in self.products 
            if product.category.lower() == category.lower()
        ]

    def find_out_of_stock_products(self):
        """
        Tìm các sản phẩm hết hàng (stock = 0)
        """
        out_of_stock_products = [
            product for product in self.products 
            if product.stock == 0
        ]
        
        if not out_of_stock_products:
            print("Không có sản phẩm nào hết hàng.")
            return []
        
        print("Các sản phẩm hết hàng:")
        for product in out_of_stock_products:
            print(f"ID: {product.id}")
            print(f"Tên: {product.name}")
            print(f"Danh mục: {product.category}")
            print("---")
        
        return out_of_stock_products

    def calculate_inventory_value_by_category(self):
        """
        Tính tổng giá trị kho hàng theo từng danh mục
        """
        category_inventory_value = {}
        
        for product in self.products:
            category = product.category
            inventory_value = product.price * product.stock
            
            category_inventory_value[category] = category_inventory_value.get(
                category, 0) + inventory_value
        
        print("Tổng giá trị kho hàng theo danh mục:")
        for category, value in category_inventory_value.items():
            print(f"{category}: {value:,} VND")
        
        return category_inventory_value

    def find_most_expensive_product_in_category(self, category):
        """
        Tìm sản phẩm đắt nhất trong một danh mục
        """
        # Lọc sản phẩm theo danh mục
        category_products = [
            product for product in self.products 
            if product.category.lower() == category.lower()
        ]
        
        # Kiểm tra nếu không có sản phẩm trong danh mục
        if not category_products:
            print(f"Không có sản phẩm trong danh mục {category}")
            return None
        
        # Tìm sản phẩm có giá cao nhất
        most_expensive_product = max(
            category_products, 
            key=lambda product: product.price
        )
        
        # Hiển thị thông tin sản phẩm đắt nhất
        print(f"\nSản phẩm đắt nhất trong danh mục {category}:")
        print(f"ID: {most_expensive_product.id}")
        print(f"Tên: {most_expensive_product.name}")
        print(f"Giá: {most_expensive_product.price:,} VND")
        print(f"Tồn kho: {most_expensive_product.stock}")
        
        return most_expensive_product

def main():
    # Khởi tạo quản lý sản phẩm
    product_manager = ProductManager()

    while True:
        print("\n--- QUẢN LÝ SẢN PHẨM ---")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm sản phẩm theo ID")
        print("6. Lọc sản phẩm theo danh mục")
        print("7. Tìm sản phẩm hết hàng")
        print("8. Tính tổng giá trị kho hàng")
        print("9. Tìm sản phẩm đắt nhất theo danh mục")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            product_manager.display_products()
        elif choice == '2':
            # Thêm sản phẩm mới
            id = int(input("Nhập ID sản phẩm: "))
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            category = input("Nhập danh mục: ")
            stock = int(input("Nhập số lượng tồn kho: "))
            
            new_product = Product(id, name, price, category, stock)
            product_manager.add_product(new_product)
        elif choice == '3':
            # Cập nhật sản phẩm
            id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            name = input("Nhập tên sản phẩm mới: ")
            price = float(input("Nhập giá sản phẩm mới: "))
            category = input("Nhập danh mục mới: ")
            stock = int(input("Nhập số lượng tồn kho mới: "))
            
            updated_product = Product(id, name, price, category, stock)
            product_manager.update_product(id, updated_product)
        elif choice == '4':
            # Xóa sản phẩm
            id = int(input("Nhập ID sản phẩm cần xóa: "))
            product_manager.delete_product(id)
        elif choice == '5':
            # Tìm sản phẩm theo ID
            id = int(input("Nhập ID sản phẩm cần tìm: "))
            found_product = product_manager.find_product_by_id(id)
            if found_product:
                print(f"Tên: {found_product.name}")
                print(f"Giá: {found_product.price:,} VND")
                print(f"Danh mục: {found_product.category}")
                print(f"Tồn kho: {found_product.stock}")
        elif choice == '6':
            # Lọc sản phẩm theo danh mục
            category = input("Nhập danh mục cần lọc: ")
            filtered_products = product_manager.filter_products_by_category(category)
            for product in filtered_products:
                print(f"{product.name} - {product.price:,} VND")
        elif choice == '7':
            # Tìm sản phẩm hết hàng
            product_manager.find_out_of_stock_products()
        elif choice == '8':
            # Tính tổng giá trị kho hàng
            product_manager.calculate_inventory_value_by_category()
        elif choice == '9':
            # Tìm sản phẩm đắt nhất theo danh mục
            category = input("Nhập danh mục cần tìm sản phẩm đắt nhất: ")
            product_manager.find_most_expensive_product_in_category(category)
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()

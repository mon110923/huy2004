# simple_events.py
class Event:
    def __init__(self):
        self._handlers = []

    def subscribe(self, handler):
        if handler not in self._handlers:
            self._handlers.append(handler)
        return self

    def unsubscribe(self, handler):
        self._handlers = [h for h in self._handlers if h != handler]
        return self

    def emit(self, *args):
        for handler in self._handlers:
            handler(*args)

def main():
    user_event = Event()

    # Định nghĩa các hàm xử lý
    def handler1(*args):
        print(f"Handler 1 received: {args}")

    def handler2(*args):
        print(f"Handler 2 received: {args}")

    # Đăng ký các hàm xử lý
    user_event.subscribe(handler1)
    user_event.subscribe(handler2)

    # Phát sự kiện
    print("Phát sự kiện lần 1:")
    user_event.emit("Xin chào!")

    # Hủy đăng ký một hàm xử lý
    print("\nHủy đăng ký handler1")
    user_event.unsubscribe(handler1)

    # Phát sự kiện lại
    print("\nPhát sự kiện lần 2:")
    user_event.emit("Thế giới!")

    # Kiểm tra đăng ký nhiều đối số
    def multi_arg_handler(*args):
        print(f"Multi-arg handler: {args}")

    print("\nKiểm tra nhiều đối số:")
    user_event.subscribe(multi_arg_handler)
    user_event.emit(1, "hai", [3])

if __name__ == "__main__":
    main()

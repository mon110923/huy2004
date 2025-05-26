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

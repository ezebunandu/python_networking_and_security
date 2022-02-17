import threading


class thread_message(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print(self.message)


threads = []


def test():
    for i in range(10):
        message = f"I am the {i} thread"
        thread = thread_message(message=message)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    import timeit

    print(timeit.timeit("test()", setup="from __main__ import test", number=5))
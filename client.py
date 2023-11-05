import multiprocessing
import socket
import hashlib
import threading


class Finder:

    def __init__(self, md5_number, start, end):
        self.ip = "127.0.0.1"
        self.port = 8000
        self.server_socket = socket.socket()
        self.server_socket.connect((self.ip, self.port))
        self.md5_number = md5_number
        self.found = False
        self.start = start
        self.end = end

    def find_secret(self):
        for i in range(self.start, self.end):
            if self.found:
                print("a")
                break
            s = str(i).zfill(3)
            ctypes = hashlib.md5(s.encode()).hexdigest()
            if ctypes == self.md5_number:
                print("b")
                print(s)
                self.found = True
                return s


def main():
    md5_number = "060fd70a06ead2e1079d27612b84aff4"

    threads = []
    cpu_count = multiprocessing.cpu_count()
    chunk = (10000-0)//cpu_count
    for i in range(0, 10000, chunk):
        finder_obj = Finder(md5_number, i, i + chunk)

        thread = threading.Thread(target=finder_obj.find_secret)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
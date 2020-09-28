import hashlib
from datetime import datetime
if __name__ == '__main__':
    print(datetime.now())
    print(hashlib.md5("adasdas".encode()).hexdigest())
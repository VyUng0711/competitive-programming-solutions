class Scanner():
    def __generator__():
        while True:
            buffer = input().strip().split()
            for x in buffer:
                yield x
    scanner = __generator__()
    def next():
        return Scanner.scanner.__next__()

n = int(Scanner.next())
m = int(Scanner.next())
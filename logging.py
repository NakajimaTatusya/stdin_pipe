import sys
import time

k=0
try:
    buff = ''
    # while True:
    #     buff += sys.stdin.read(1)
    #     if buff.endswith('\n'):
    #         print(buff[:-1])
    #         buff = ''
    #         k = k + 1

    for line in sys.stdin.readlines():
        sys.stdout.writelines(line)
        k += 1

    # for line in sys.stdin.read(1):
    #     buff += line
    #     if buff.endswith('\n'):
    #         print(buff[:-1])
    #         buff = ''
    #         k += 1
except KeyboardInterrupt:
    pass
finally:
    sys.stdin.flush()

print(k)

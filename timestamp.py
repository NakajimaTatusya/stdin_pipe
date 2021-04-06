import os
import signal
import sys
import time

"""
target platform Unix only
"""

sys.stdin = os.fdopen(sys.stdin.fileno(), 'rb', 0)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def main():
    for arg in sys.argv[1:]:
        fh = arg == '-' and sys.stdin or open(arg, 'rb', 0)
        try:
            for line in iter(fh.readline, ''):
                sys.stdout.write(time.strftime('%F %T ') + line)
        finally:
            if fh is not sys.stdin:
                fh.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
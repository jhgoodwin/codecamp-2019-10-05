import signal
import sys
import time


def sigterm_handler(signal, frame):
    print('shutting down ...')
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    while True:
        time.sleep(100)


if __name__ == '__main__':
    main()
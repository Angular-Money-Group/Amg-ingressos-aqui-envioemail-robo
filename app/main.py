from mail_service import process_email

import time


def main():
    while True:
        process_email()
        time.sleep(20)


if __name__ == "__main__":
    main()

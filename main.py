from decouple import config

if __name__ == '__main__':
    test_read_from_env = config("MY_ENV")
    if test_read_from_env == "Yes":
        print("It works.")
    else:
        print("NOoooooo")

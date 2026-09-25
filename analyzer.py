def read_log_file(filename):
    with open(filename, "r") as file:
        for line in file:
            if "LOGIN_FAILED" in line:
                print(line.strip())


read_log_file("sample.log")
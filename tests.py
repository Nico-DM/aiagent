from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# INPUTS_INFO = [
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../")
# ]

# INPUTS_CONTENT = [
#     # ("calculator", "lorem.txt"),
#     ("calculator", "main.py"),
#     ("calculator", "pkg/calculator.py"),
#     ("calculator", "/bin/cat"),
#     ("calculator", "pkg/does_not_exist.py"),
# ]

# INPUTS_WRITE = [
#     ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
#     ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
#     ("calculator", "/tmp/temp.txt", "this should not be allowed")
# ]

INPUTS_RUN = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py")
]


def main():
    # print("Testing get_files_info function:")
    # for args in INPUTS_INFO:
    #     print(f"Result for '{args[1]}' directory:")
    #     print(get_files_info(*args))

    # print("\nTesting get_file_content function:")
    # for args in INPUTS_CONTENT:
    #     print(f"Result for '{args[1]}' file:")
    #     print(get_file_content(*args))

    # print("\nTesting write_file function:")
    # for args in INPUTS_WRITE:
    #     print(f"Result for writing '{args[2]}' to '{args[1]}' file:")
    #     print(write_file(*args))

    print("\nTesting run_python function:")
    for args in INPUTS_RUN:
        print(f"Result for running '{args[1]}' with args {args[2:]}:")
        print(run_python_file(*args))

if __name__ == "__main__":
    main()
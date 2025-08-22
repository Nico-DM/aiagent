from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
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

INPUTS_WRITE = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
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
    for args in INPUTS_WRITE:
        print(f"Result for writing '{args[2]}' to '{args[1]}' file:")
        print(write_file(*args))

if __name__ == "__main__":
    main()
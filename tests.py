from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# INPUTS_INFO = [
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../")
# ]

INPUTS_CONTENT = [
    # ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]



def main():
    # print("Testing get_files_info function:")
    # for args in INPUTS_INFO:
    #     print(f"Result for '{args[1]}' directory:")
    #     print(get_files_info(*args))

    # print("\nTesting get_file_content function:")
    for args in INPUTS_CONTENT:
        print(f"Result for '{args[1]}' file:")
        print(get_file_content(*args))

if __name__ == "__main__":
    main()
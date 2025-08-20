from functions.get_files_info import get_files_info

INPUTS = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
]



def main():
    for args in INPUTS:
        print(f"Result for '{args[1]}' directory:")
        print(get_files_info(*args))

if __name__ == "__main__":
    main()
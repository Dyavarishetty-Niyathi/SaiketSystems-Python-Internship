def read_file(filename):
    # Reads file content safely.
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(" Error: File not found. Make sure the file exists.")
        return None
    except Exception as e:
        print(f" Unexpected error while reading file: {e}")
        return None


def write_file(filename, data):
    # Writes modified text back to the file.
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(" File updated successfully!")
    except Exception as e:
        print(f" Error while writing to file: {e}")


def find_and_replace(text, find_word, replace_word):
    # Replaces all occurrences of a word in the text.
    if find_word not in text:
        print(f" '{find_word}' not found in the file.")
    return text.replace(find_word, replace_word)


def main():

    filename = input("Enter the filename (example: sample.txt): ")

    content = read_file(filename)

    if content is None:
        return

    print("\n Original File Content")
    print(content)
    print("\n")

    find_word = input("Enter the word you want to find: ")
    replace_word = input("Enter the word to replace it with: ")

    updated_content = find_and_replace(content, find_word, replace_word)

    print("\n Updated Content")
    print(updated_content)


    write_file(filename, updated_content)


if __name__ == "__main__":
    main()
from collections import Counter

def read_file(filename):
    # Reads the content of a file and returns it as a string.
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(" Error: File not found.")
        return None
    except Exception as e:
        print(f" Unexpected error: {e}")
        return None


def analyze_text(text):
    # Analyzes text for lines, words, characters and frequency.
    
    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    # Convert all words to lowercase for accurate frequency count
    word_freq = Counter(word.lower() for word in words)

    return lines, words, characters, word_freq


def display_results(lines, words, characters, word_freq):
    # Displays the results in a clean, structured format.
    print("\n Text analysis report")
    print(f"Total Lines      : {len(lines)}")
    print(f"Total Words      : {len(words)}")
    print(f"Total Characters : {characters}")
    print("\n Most Common Words:")

    for word, count in word_freq.most_common(10):
        print(f"{word:<15} → {count} times")


def main():
    print(" Word count and frequency analyser")

    filename = input("Enter filename (e.g., sample.txt): ")
    content = read_file(filename)

    if content is None:
        return

    lines, words, characters, freq = analyze_text(content)
    display_results(lines, words, characters, freq)


if __name__ == "__main__":
    main()

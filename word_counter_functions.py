def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence and returns it as a string.

    Returns:
        str: The user's input sentence.
    """
    return input("Enter a sentence: ").strip()

def count_words(sentence: str) -> int:
    """
    Counts the number of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The number of words in the sentence.
    """
    return len(sentence.split())

def main():
    """
    Main function to get user input, count words, and display the result.
    """
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} word{'s' if word_count != 1 else ''}.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
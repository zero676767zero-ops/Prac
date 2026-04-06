def soundex(word):
    # Handle empty input
    if not word:
        return ""

    word = word.upper()

    # Soundex mapping
    soundex_map = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6"
    }

    first_letter = word[0]

    encoded_digits = ""
    previous_digit = ""

    # Process remaining characters
    for char in word[1:]:
        digit = soundex_map.get(char, "")  # safer lookup

        # Avoid consecutive duplicates
        if digit != previous_digit:
            encoded_digits += digit

        previous_digit = digit

    # Combine first letter with digits
    soundex_code = first_letter + encoded_digits

    # Pad or trim to 4 characters
    soundex_code = (soundex_code + "000")[:4]

    return soundex_code


# Test words
test_words = ["Robert", "Rupert", "Ruia", "Herman", "Hermann"]

for word in test_words:
    print(word, "=>", soundex(word))
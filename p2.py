# 1)Edit distance between strings s1 and s2
def edit_distance_recursive(str1, str2, len1, len2):
    # Base cases
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    # If last characters match
    if str1[len1 - 1] == str2[len2 - 1]:
        return edit_distance_recursive(str1, str2, len1 - 1, len2 - 1)

    # If last characters don't match
    return 1 + min(
        edit_distance_recursive(str1, str2, len1, len2 - 1),    # Insert
        edit_distance_recursive(str1, str2, len1 - 1, len2),    # Delete
        edit_distance_recursive(str1, str2, len1 - 1, len2 - 1) # Replace
    )


# Input
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

distance = edit_distance_recursive(string1, string2, len(string1), len(string2))
print("Edit Distance:", distance)

# weighted edit distance between strings s1 and s2
import numpy as np

def levenshtein_distance(str1, str2):
    rows = len(str1) + 1
    cols = len(str2) + 1

    # Create matrix
    dp_matrix = np.zeros((rows, cols), dtype=int)

    # Initialize first row and column
    for i in range(rows):
        dp_matrix[i][0] = i
    for j in range(cols):
        dp_matrix[0][j] = j

    # Fill matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i - 1] == str2[j - 1]:
                dp_matrix[i][j] = min(
                    dp_matrix[i - 1][j] + 1,      # Delete
                    dp_matrix[i - 1][j - 1],      # Match
                    dp_matrix[i][j - 1] + 1       # Insert
                )
            else:
                dp_matrix[i][j] = min(
                    dp_matrix[i - 1][j] + 1,      # Delete
                    dp_matrix[i - 1][j - 1] + 1,  # Replace
                    dp_matrix[i][j - 1] + 1       # Insert
                )

    print("DP Matrix:\n", dp_matrix)
    return dp_matrix[rows - 1][cols - 1]


print("Levenshtein Distance:", levenshtein_distance("cat", "dog"))


# 3)   Two sentences are given. Compute the edit distance at the word level:

# Sentence 1: I love natural language processing
# Sentence 2: I enjoy learning language processing

def word_edit_distance(words1, words2, len1, len2):
    # Base cases
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    # If words match
    if words1[len1 - 1] == words2[len2 - 1]:
        return word_edit_distance(words1, words2, len1 - 1, len2 - 1)

    # If words don't match
    return 1 + min(
        word_edit_distance(words1, words2, len1, len2 - 1),    # Insert
        word_edit_distance(words1, words2, len1 - 1, len2),    # Delete
        word_edit_distance(words1, words2, len1 - 1, len2 - 1) # Replace
    )


# Input
sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

# Convert to word lists
words_list1 = sentence1.split()
words_list2 = sentence2.split()

distance = word_edit_distance(words_list1, words_list2, len(words_list1), len(words_list2))

print("Word-level Edit Distance:", distance)
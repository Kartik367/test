def create_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace 'J' with 'I'
    key = ''.join(dict.fromkeys(key))    # Remove duplicates while preserving order
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Alphabet excluding 'J'
    
    # Create a 5x5 matrix
    matrix = [char for char in key if char in alphabet] + [char for char in alphabet if char not in key]
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair_cipher(text, key):
    matrix = create_matrix(key)  # Create the Playfair matrix
    text = text.upper().replace("J", "I").replace(" ", "")  # Prepare text

    # Add 'X' if the text length is odd
    if len(text) % 2 != 0:
        text += 'X'

    cipher = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]  # Get pairs of characters
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        # Apply Playfair rules
        if row_a == row_b:  # Same row
            cipher += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:  # Same column
            cipher += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:  # Rectangle case
            cipher += matrix[row_a][col_b] + matrix[row_b][col_a]

    return cipher

# Example usage
key = "playfair example"
text = "hide the gold"
print("Ciphered Text:", playfair_cipher(text, key))

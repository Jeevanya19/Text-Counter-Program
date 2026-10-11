
# Word and Character Counter

text = input("Enter a paragraph: ")

# Count characters
characters = len(text)

# Count words
words = len(text.split())

# Count sentences
sentences = 0
for mark in ".!?":
    sentences += text.count(mark)

# Count spaces
spaces = text.count(" ")

# Display results
if text.strip() == "":
    print("\nNo text entered!")
else:
    print("\n--- Text Analysis Results ---")
    print("Characters:", characters)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Spaces:", spaces)

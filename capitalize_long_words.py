def capitalize_long(words):
    return [word.upper() if len(word) > 5 else word for word in words]

words = ["hello", "world", "python", "programming", "is", "fun"]

result = capitalize_long(words)
print(result)
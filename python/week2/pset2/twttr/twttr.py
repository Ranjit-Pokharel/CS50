# prompting the user for input
text = input("Enter a string of text: ")

# useing a list comprehension to remove vowels (both uppercase and lowercase)
text_without_vowels = ''.join([char for char in text if char.lower() not in 'aeiouAEIOU'])

print(text_without_vowels)

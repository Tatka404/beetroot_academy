morse_code = {
    'А': '·–',
    'Б': '–···',
    'В': '·––',
    'Г': '––·',
    'Д': '–··',
    'Е': '·',
    'Ж': '···–',
    'З': '––··',
    'И': '··',
    'Й': '·–––',
    'К': '–·–',
    'Л': '·–··',
    'М': '––',
    'Н': '–·',
    'О': '–––',
    'П': '·––·',
    'Р': '·–·',
    'С': '···',
    'Т': '–',
    'У': '··–',
    'Ф': '··–·',
    'Х': '····',
    'Ц': '–·–·',
    'Ч': '–––·',
    'Ш': '––––',
    'Щ': '––·–',
    'Ы': '–·––',
    ('Ь', 'Ъ'): '–··–',
    # 'Ь': '–··–',
    # 'Ъ': '–··–',
    'Э': '··–··',
    'Ю': '··––',
    'Я': '·–·–'
}

words = input("Enter a word/phrase to be morsen: ")
words_morse = ' '.join(morse_code[char] for char in words.upper())
try:
    print(words_morse)
except KeyError:
    print('Invalid character!')


morse_code_reverse = {value: key for key, value in morse_code.items()}
print(' '.join(morse_code_reverse.get(char) for char in words_morse.split()))

print(morse_code_reverse)


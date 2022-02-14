poem_text = (input('Type down your favourite poem text: ')).lower()


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print('Occurrences of each word in your favourite poem text is:', word_count(poem_text))

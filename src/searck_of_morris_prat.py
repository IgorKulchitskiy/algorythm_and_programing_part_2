
#7
def table_prefix(pattern, m):
    prefix_table = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1
    return prefix_table

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    indices = []

    prefix_table = table_prefix(pattern, m)

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = prefix_table[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return indices

text = "Привіт Василь"
pattern = "Василь"
print("Індекси входжень:", kmp_search(text, pattern))

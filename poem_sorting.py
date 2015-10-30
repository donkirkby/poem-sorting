def sort_words(text):
    words = text.lower().split()
    sorted_words = map(''.join, map(sorted, words))
    return ' '.join(sorted_words)


def main():
    with open('poems/whitman.md', 'rU') as f:
        poem = []
        poems = set()
        for line in f:
            if line.startswith('#'):
                if poem:
                    poems.add('\n\n\n'.join(poem))
                    poem = []
            elif line.strip():
                sorted_line = sort_words(line)
                poem.append(sorted_line)
        if poem:
            poems.add('\n\n\n'.join(poem))

    with open('emop-ginorst.md', 'w') as f:
        for poem in poems:
            f.write(poem)
            f.write('\n\n\n\n---\n\n\n\n')
    print('Done.')
main()

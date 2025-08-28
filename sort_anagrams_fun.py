def sort_anagrams(list_of_strings: list[str]) -> list[list[str]]:
    """Returns a list of anagram lists from list of strings"""
    result = []
    used = set()
    for word in list_of_strings:
        if word in used:
            continue
        anagrams = [w for w in list_of_strings if sorted(word) == sorted(w)]
        result.append(anagrams)
        used.update(anagrams)
    return result

def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))

if __name__ == '__main__':
    main()
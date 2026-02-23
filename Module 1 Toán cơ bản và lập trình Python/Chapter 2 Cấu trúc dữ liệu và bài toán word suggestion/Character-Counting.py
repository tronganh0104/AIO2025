def character_counting(character):
    result = {}
    for c in character:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result
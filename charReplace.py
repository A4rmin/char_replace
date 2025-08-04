def charReplace(name1,name2):
    replacements = {'i': '1', 'a': '4', 's': '5'}
    # Basic replacements for characters
    def replace_char(name):
        result = ""
        for char in name:
            if char in replacements:
                result += replacements[char]
            else:
                result += char

        return result

    name1 = replace_char(name1)
    name2 = replace_char(name2)
    print(name1, name2)
    return name1, name2

charReplace("armin", "sara")
# 4rm1n 54r4
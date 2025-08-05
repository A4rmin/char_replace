# Basic replacements for characters
def replace_char(name):
    LowerCaseName = name.lower()
    replacements = {'i': '1', 'a': '4', 's': '5'}
    result = ""
    for char in LowerCaseName:
        if char in replacements:
            result += replacements[char]
        else:
            result += char
    return result

# print(replace_char("Armin Sara"))  # Example usage
    # 4rm1n 54r4
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivan", "Julia"]
count = 0
for i in names:
    count += 1
    print("Mame_number:", count)
    print("Original_name:", i)
    print("Modified_name:", replace_char(i))


print("total:", count)


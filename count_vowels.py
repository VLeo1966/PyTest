def count_vowels(input_str):
    vowels = "аеёийоуыэюяАЕЁИЙОУЫЭЮЯ"
    return sum(1 for char in input_str if char in vowels)

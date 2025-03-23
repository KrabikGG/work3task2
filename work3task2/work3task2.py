word = input("Введіть слово: ")

duplicates = set()
seen = set()

for letter in word:
    if letter in seen:
        duplicates.add(letter)
    else:
        seen.add(letter)

if duplicates:
    print("Повторювані літери:", ", ".join(sorted(duplicates)))
else:
    print("У слові немає повторюваних літер.")
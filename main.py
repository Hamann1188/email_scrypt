data = """
test-test@rambler.ru:password
test2test2@rambler.ru:password2
... (остальной список)
"""

# Разбиваем строки
lines = data.strip().split("\n")

# Преобразуем каждую строку
result = []
for line in lines:
    email, password = line.split(":")
    result.append(f"{email}:GhodMoon423:{email}:{password}")

# Выводим результат
print("\n".join(result))

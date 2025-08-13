# Примеры использования rsplit (split right)

# rsplit() разделяет строку справа налево
text = "apple.banana.cherry.date"

# Обычный split (слева направо)
print("split():", text.split('.', 2))  # ['apple', 'banana', 'cherry.date']

# rsplit (справа налево) 
print("rsplit():", text.rsplit('.', 2))  # ['apple.banana', 'cherry', 'date']

# Пример с путем к файлу
filepath = "C:/Users/Documents/file.txt"
print("Имя файла:", filepath.rsplit('/', 1)[-1])  # file.txt
print("Директория:", filepath.rsplit('/', 1)[0])  # C:/Users/Documents
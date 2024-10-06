import re

def find_z_words(text):
    """
    Задача 1: Находит все слова, начинающиеся на 'z' или 'Z'.
    """
    return re.findall(r'\b[zZ]\w+', text)

def extract_titles(text):
    """
    Задача 2: Извлекает заголовки из пронумерованного списка.
    """
    return re.findall(r'\d+\.\s*(.+)', text)

def split_text_and_numbers(text):
    """
    Задача 3: Разделяет текст на слова и числа.
    """
    pattern = r'\d+|\D+'
    return [int(match) if match.isdigit() else match.strip() for match in re.findall(pattern, text)]

# Примеры использования функций
print(find_z_words("Zookeepers zoom in on little zebras"))
print(extract_titles("1. First title 2. Second title 3. Third title"))
print(split_text_and_numbers("We had 100 grams of coconut powder 200 kilos of math"))

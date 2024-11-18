import string

class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация объекта класса. Принимает произвольное количество файлов и сохраняет их имена.
        """
        self.file_names = file_names

    def get_all_words(self):
        """
        Читает файлы, удаляет пунктуацию, переводит текст в нижний регистр и создает словарь,
        где ключ - имя файла, значение - список слов из этого файла.
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    # Удаление пунктуации
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл отсутствует, возвращаем пустой список
        return all_words

    def find(self, word):
        """
        Ищет первое вхождение слова в каждом файле.
        Возвращает словарь, где ключ - имя файла, значение - позиция первого вхождения (1-based индекс).
        Если слово не найдено, возвращает None для файла.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            try:
                result[name] = words.index(word) + 1  # Преобразуем в индекс с 1
            except ValueError:
                result[name] = None  # Слово не найдено
        return result

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле.
        Возвращает словарь, где ключ - имя файла, значение - количество вхождений слова.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {name: words.count(word) for name, words in all_words.items()}
        return result

# Пример использования:
# Создаем тестовый файл для проверки
test_filename = "test_file.txt"
with open(test_filename, "w", encoding="utf-8") as file:
    file.write("It's a text for task. Найти везде! Используйте его для самопроверки. Успехов в решении задачи. text text text")

import string

class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация объекта класса. Принимает произвольное количество файлов и сохраняет их имена.
        """
        self.file_names = file_names

    def get_all_words(self):
        """
        Читает файлы, удаляет пунктуацию, переводит текст в нижний регистр и создает словарь,
        где ключ - имя файла, значение - список слов из этого файла.
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    # Удаление пунктуации
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ', '—', '’']:
                        content = content.replace(punct, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []  # Если файл отсутствует, возвращаем пустой список
        return all_words

    def find(self, word):
        """
        Ищет первое вхождение слова в каждом файле.
        Возвращает словарь, где ключ - имя файла, значение - позиция первого вхождения (1-based индекс).
        Если слово не найдено, возвращает None для файла.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            try:
                result[name] = words.index(word) + 1  # Преобразуем в индекс с 1
            except ValueError:
                result[name] = None  # Слово не найдено
        return result

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле.
        Возвращает словарь, где ключ - имя файла, значение - количество вхождений слова.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {name: words.count(word) for name, words in all_words.items()}
        return result


# Основной код для тестирования
if __name__ == "__main__":
    # Примеры использования

    # Создайте файлы test_file.txt и captain.txt в папке проекта
    finder = WordsFinder('test_file.txt', 'captain.txt')

    # Получить все слова из файлов
    print("Все слова из файлов:")
    print(finder.get_all_words())

    # Найти первое вхождение слова "Captain"
    print("\nПервое вхождение слова 'Captain':")
    print(finder.find("Captain"))

    # Посчитать количество вхождений слова "Captain"
    print("\nКоличество вхождений слова 'Captain':")
    print(finder.count("Captain"))
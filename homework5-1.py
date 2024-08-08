class HashTable:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size of hash table must be a positive integer.")
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        if key is None:
            raise ValueError("Key must not be None.")
        return hash(key) % self.size

    def insert(self, key, value):
        try:
            key_hash = self.hash_function(key)
            key_value = [key, value]

            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            self.table[key_hash].append(key_value)
            return True
        except Exception as e:
            print(f"An error occurred while inserting: {e}")
            return False

    def get(self, key):
        try:
            key_hash = self.hash_function(key)
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None
        except Exception as e:
            print(f"An error occurred while retrieving: {e}")
            return None

    def delete(self, key):
        try:
            key_hash = self.hash_function(key)
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove(pair)
                    return True
            return False
        except Exception as e:
            print(f"An error occurred while deleting: {e}")
            return False

if __name__ == '__main__':
    try:
        # Тестуємо нашу хеш-таблицю:
        H = HashTable(5)
        H.insert("apple", 10)
        H.insert("orange", 20)
        H.insert("banana", 30)
        H.insert("apple", 50)

        print(H.get("apple"))   # Виведе: 50
        print(H.get("orange"))  # Виведе: 20
        print(H.get("banana"))  # Виведе: 30

        # Видаляємо один елемент і перевіряємо його відсутність
        H.delete("apple")
        print(H.get("apple"))  # Виведе: None
        print(H.table)         # Виведе таблицю без елемента з ключем "apple"
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

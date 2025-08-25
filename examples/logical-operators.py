"""
Примеры логических операций в Python
Демонстрация основных логических концепций для программистов
"""

def demonstrate_basic_operators():
    """Демонстрация базовых логических операторов"""
    print("=== Базовые логические операторы ===")
    
    # Конъюнкция (И)
    a = True
    b = False
    print(f"Конъюнкция (AND): {a} AND {b} = {a and b}")
    print(f"Конъюнкция (AND): {a} AND {a} = {a and a}")
    
    # Дизъюнкция (ИЛИ)
    print(f"Дизъюнкция (OR): {a} OR {b} = {a or b}")
    print(f"Дизъюнкция (OR): {b} OR {b} = {b or b}")
    
    # Отрицание (НЕ)
    print(f"Отрицание (NOT): NOT {a} = {not a}")
    print(f"Отрицание (NOT): NOT {b} = {not b}")
    
    # Импликация (ЕСЛИ-ТО)
    def implication(p, q):
        """Импликация: если p, то q"""
        return (not p) or q
    
    print(f"Импликация: {a} -> {b} = {implication(a, b)}")
    print(f"Импликация: {a} -> {a} = {implication(a, a)}")
    
    # Эквиваленция (ТОГДА И ТОЛЬКО ТОГДА)
    def equivalence(p, q):
        """Эквиваленция: p тогда и только тогда, когда q"""
        return p == q
    
    print(f"Эквиваленция: {a} <-> {b} = {equivalence(a, b)}")
    print(f"Эквиваленция: {a} <-> {a} = {equivalence(a, a)}")


def truth_table_example():
    """Построение таблицы истинности"""
    print("\n=== Таблица истинности для (p AND q) OR (NOT p) ===")
    
    def logical_expression(p, q):
        """Логическое выражение: (p AND q) OR (NOT p)"""
        return (p and q) or (not p)
    
    print("p\tq\tp AND q\tNOT p\t(p AND q) OR (NOT p)")
    print("-" * 50)
    
    for p in [True, False]:
        for q in [True, False]:
            p_and_q = p and q
            not_p = not p
            result = logical_expression(p, q)
            print(f"{p}\t{q}\t{p_and_q}\t{not_p}\t{result}")


def logical_laws_demonstration():
    """Демонстрация логических законов"""
    print("\n=== Логические законы ===")
    
    # Закон тождества: A = A
    a = True
    print(f"Закон тождества: {a} = {a} -> {a == a}")
    
    # Закон противоречия: A AND NOT A = False
    print(f"Закон противоречия: {a} AND NOT {a} = {a and (not a)}")
    
    # Закон исключенного третьего: A OR NOT A = True
    print(f"Закон исключенного третьего: {a} OR NOT {a} = {a or (not a)}")
    
    # Закон двойного отрицания: NOT (NOT A) = A
    print(f"Закон двойного отрицания: NOT (NOT {a}) = {not (not a)}")
    
    # Законы де Моргана
    p, q = True, False
    print(f"Закон де Моргана 1: NOT ({p} AND {q}) = NOT {p} OR NOT {q}")
    print(f"Результат: {not (p and q)} = {not p or not q}")
    
    print(f"Закон де Моргана 2: NOT ({p} OR {q}) = NOT {p} AND NOT {q}")
    print(f"Результат: {not (p or q)} = {not p and not q}")


def practical_programming_examples():
    """Практические примеры использования логики в программировании"""
    print("\n=== Практические примеры ===")
    
    # Пример 1: Проверка условий доступа
    user_age = 25
    user_has_id = True
    user_is_banned = False
    
    can_access = (user_age >= 18 and user_has_id) and not user_is_banned
    print(f"Пользователь может получить доступ: {can_access}")
    
    # Пример 2: Валидация данных
    email = "user@example.com"
    password = "password123"
    
    is_valid_email = "@" in email and "." in email
    is_valid_password = len(password) >= 8 and any(c.isdigit() for c in password)
    
    can_register = is_valid_email and is_valid_password
    print(f"Можно зарегистрироваться: {can_register}")
    
    # Пример 3: Обработка ошибок
    file_exists = True
    file_readable = False
    
    if file_exists and file_readable:
        print("Файл можно прочитать")
    elif file_exists and not file_readable:
        print("Файл существует, но недоступен для чтения")
    elif not file_exists:
        print("Файл не существует")
    else:
        print("Неожиданная ситуация")


def logical_functions():
    """Реализация логических функций"""
    print("\n=== Логические функции ===")
    
    def xor(p, q):
        """Исключающее ИЛИ (XOR)"""
        return (p or q) and not (p and q)
    
    def nand(p, q):
        """И-НЕ (NAND)"""
        return not (p and q)
    
    def nor(p, q):
        """ИЛИ-НЕ (NOR)"""
        return not (p or q)
    
    # Демонстрация функций
    p, q = True, False
    print(f"XOR({p}, {q}) = {xor(p, q)}")
    print(f"NAND({p}, {q}) = {nand(p, q)}")
    print(f"NOR({p}, {q}) = {nor(p, q)}")
    
    # Демонстрация универсальности NAND
    print(f"\nУниверсальность NAND:")
    print(f"NOT p = NAND(p, p): {not p} = {nand(p, p)}")
    print(f"p AND q = NOT NAND(p, q): {p and q} = {not nand(p, q)}")
    print(f"p OR q = NAND(NOT p, NOT q): {p or q} = {nand(not p, not q)}")


def error_detection_example():
    """Пример использования логики для обнаружения ошибок"""
    print("\n=== Обнаружение ошибок ===")
    
    # Простая система контроля четности
    def calculate_parity(data):
        """Вычисление бита четности"""
        return sum(data) % 2
    
    def check_parity(data, parity_bit):
        """Проверка бита четности"""
        calculated_parity = calculate_parity(data)
        return calculated_parity == parity_bit
    
    # Пример использования
    data = [1, 0, 1, 1, 0]
    parity_bit = calculate_parity(data)
    print(f"Данные: {data}")
    print(f"Бит четности: {parity_bit}")
    
    # Проверка без ошибок
    is_correct = check_parity(data, parity_bit)
    print(f"Данные корректны: {is_correct}")
    
    # Проверка с ошибкой
    corrupted_data = [1, 0, 1, 0, 0]  # Изменен один бит
    is_correct_corrupted = check_parity(corrupted_data, parity_bit)
    print(f"Искаженные данные корректны: {is_correct_corrupted}")


if __name__ == "__main__":
    """Запуск всех демонстраций"""
    print("Демонстрация логических операций в Python")
    print("=" * 50)
    
    demonstrate_basic_operators()
    truth_table_example()
    logical_laws_demonstration()
    practical_programming_examples()
    logical_functions()
    error_detection_example()
    
    print("\n" + "=" * 50)
    print("Демонстрация завершена!")

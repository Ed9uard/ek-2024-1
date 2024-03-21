import sys
from datetime import datetime


def parse_log_line(line: str) -> dict:
    try:
        parts = line.split(' ', maxsplit=3)
        if len(parts) < 4:
            raise ValueError(" Недостатньо компонентів у рядку логу")
        timestamp = datetime.strptime(parts[0] + ' ' + parts[1], '%Y-%m-%d %H:%M:%S')
        level = parts[2]
        message = parts[3].strip()
        return {'timestamp': timestamp, 'level': level, 'message': message}
    except ValueError as e:
        print(f" Помилка при парсингу рядка логу: {e}")
        return None


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    
    valid_levels = {'INFO', 'ERROR', 'DEBUG', 'WARNING'}
    if level.upper() not in valid_levels:
        print(f"Недійсний рівень логування '{level}'. Доступні рівні: {', '.join(valid_levels)}")
        return []
    return [log for log in logs if log['level'] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Введіть шлях до файлу логів.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    if not logs:
        sys.exit(1)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()  # Перетворюємо рівень логування в верхній регістр
        valid_levels = {'INFO', 'ERROR', 'DEBUG', 'WARNING'}
        if level not in valid_levels:
            print(f"Недійсний рівень логування '{level}'. Доступні рівні: {', '.join(valid_levels)}")
        else:
            logs = filter_logs_by_level(logs, level)
            print(f"\n Деталі логів для рівня '{level}':")
            if logs:
                for log in logs:
                    print(f"{log['timestamp']} - {log['message']}")
            else:
                print(f"Відсутні записи для рівня '{level}'.")
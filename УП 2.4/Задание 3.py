import psutil
import sqlite3
from datetime import datetime
import time

def init_db():
    conn = sqlite3.connect("monitoring.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    cpu_usage REAL,
                    memory_usage REAL,
                    disk_usage REAL
                )''')
    conn.commit()
    conn.close()

def log_system_stats():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    conn = sqlite3.connect("monitoring.db")
    c = conn.cursor()
    c.execute("INSERT INTO system_stats (timestamp, cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?, ?)",
              (timestamp, cpu, memory, disk))
    conn.commit()
    conn.close()
    print(f"[{timestamp}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

def view_stats():
    conn = sqlite3.connect("monitoring.db")
    c = conn.cursor()
    c.execute("SELECT * FROM system_stats ORDER BY timestamp DESC LIMIT 20")
    rows = c.fetchall()
    for row in rows:
        print(f"{row[1]} | CPU: {row[2]}% | Memory: {row[3]}% | Disk: {row[4]}%")
    conn.close()

def menu():
    while True:
        print("\n===== Системный монитор =====")
        print("1. Записать текущее состояние")
        print("2. Просмотреть последние записи")
        print("3. Автоматический мониторинг (повторяем)")
        print("4. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            log_system_stats()

        elif choice == '2':
            view_stats()

        elif choice == '3':
            try:
                cycles = input("Сколько раз собирать данные? (Enter = бесконечно, q = отмена): ")
                if cycles.lower() == 'q':
                    continue
                elif cycles == '':
                    print("Бесконечный режим.")
                    while True:
                        log_system_stats()
                        time.sleep(5)
                else:
                    cycles = int(cycles)
                    for _ in range(cycles):
                        log_system_stats()
                        time.sleep(5)
            except KeyboardInterrupt:
                print("\nМониторинг остановлен.")
            except ValueError:
                print("Ошибка: введите число или оставьте пустым для бесконечного режима.")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    init_db()
    menu()

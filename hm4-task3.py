import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory(directory):
    direct_path = Path(directory)
    
    if not (direct_path.exists() and direct_path.is_dir()):
        print(f"{Fore.RED}Помилка: {directory} не є дійсним каталогом.{Style.RESET_ALL}")
        return
    
    print(f"{Fore.BLACK}Перелік структури каталогу: {directory}{Style.RESET_ALL}")
    
    try:
        for item in direct_path.iterdir():
            if item.is_dir():
                print(f"{Fore.GREEN}[Directory] {item.name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[File] {item.name}{Style.RESET_ALL}")
    except OSError as e:
        print(f"{Fore.RED}Помилка:{e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Використання:{sys.argv[0]}<шлях до катологу>")
        sys.exit(1)
        
    direct_path = sys.argv[1]
    visualize_directory(direct_path)
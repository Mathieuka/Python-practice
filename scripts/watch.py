import subprocess

def start_watcher():
    try:
        command = [
            'watchmedo',
            'shell-command',
            '--patterns=*.py',
            '--recursive',
            '--command=python3 main.py'
        ]

        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("Watcher stopped.")

if __name__ == '__main__':
    start_watcher()
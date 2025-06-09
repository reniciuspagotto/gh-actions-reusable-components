import sys

def main():
    message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from Python!"
    print(message)

if __name__ == "__main__":
    main()
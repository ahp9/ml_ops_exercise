import typer

def main(count: int = 1):
    for _ in range(count):
        print("Hello, World!")

if __name__ == "__main__":
    typer.run(main)

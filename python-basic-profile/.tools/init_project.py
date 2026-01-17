import os

# Define the folder structure
folders = [
    "src/app",
    "tests",
    "notebooks",
]

files = {
    "src/app/__init__.py": "",
    "src/app/main.py": 'def hello():\n    return "hello world"\n',
    "tests/test_main.py": (
        "from app.main import hello\n\n"
        "def test_hello():\n"
        "    assert hello() == 'hello world'\n"
    ),
    "notebooks/.gitkeep": "",
    "pyproject.toml": (
        "[tool.black]\n"
        "line-length = 88\n\n"
        "[tool.flake8]\n"
        "max-line-length = 88\n\n"
        "[tool.mypy]\n"
        "strict = true\n\n"
        "[tool.pytest.ini_options]\n"
        "pythonpath = [\"src\"]\n"
    ),
    "README.md": "# python-basic-profile project\n",
    "Makefile": (
        "format:\n\tblack src tests\n\n"
        "lint:\n\tflake8 src tests\n\n"
        "typecheck:\n\tmypy src\n\n"
        "test:\n\tpytest\n"
    ),
}

def main():
    print("Creating project structure...")

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for path, content in files.items():
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)
            print(f"Created file: {path}")
        else:
            print(f"Skipped existing file: {path}")

    print("\nProject structure initialized successfully.")

if __name__ == "__main__":
    main()

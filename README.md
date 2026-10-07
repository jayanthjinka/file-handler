# File Handler

## Description

File Handler is a Python program that reads data from a text file, finds a specified word, replaces it with a specified word, and saves the modified data back to the same text file.

The project demonstrates Python file input/output, string manipulation, and file-related exception handling.

## Features

- Reads contents from a plain-text file
- Finds a specified word in the file data
- Replaces the specified word with another word
- Saves the modified contents back to the same file
- Handles common file-related errors gracefully

## Prerequisites

- Python 3.x
- No external packages

## Usage

Run the program from the project directory:

```bash
python3 main.py
```

The program asks for:

1. The word to find
2. The replacement word

The modified content is saved back to `data.txt`.

## Project Structure

```text
file-handler/
├── main.py
├── data.txt
└── README.md
```

- `main.py` - contains the Python program
- `data.txt` - plain-text input/output file
- `README.md` - project documentation

## Examples

Initial `data.txt`:

```text
Hello World
I am Jayanth Jinka
I am pursuing a B.Tech CSE AIML
```

Run:

```bash
python3 main.py
```

For example:

```text
Enter the word to find: Jayanth Jinka
Enter the replacement word: Jay
```

The resulting `data.txt` will be:

```text
Hello World
I am Jay
I am pursuing a B.Tech CSE AIML
```

## Error Handling

The program handles common file-related errors, including:

- File not found
- Permission denied
- Other file operation errors

## Testing

The program was verified for:

- File reading
- Word replacement
- File writing
- Missing target word
- Missing file
- Permission failure

## Limitations

- Works with plain-text files only
- Updates the same `data.txt` file
- Uses basic console input
- No external packages or additional features

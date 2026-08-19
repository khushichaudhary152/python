# Interactive Personal Data Collector

## Overview

The **Interactive Personal Data Collector** is a beginner-friendly Python console application. It asks the user for a few personal details and then displays the collected values along with their Python data types and memory addresses. The program also calculates the user's approximate year of birth from their age.

This project demonstrates essential Python concepts, including user input, type conversion, variables, the `type()` function, the `id()` function, and simple arithmetic operations.

## Features

- Collects the user's name, age, height, and favourite number.
- Converts each input to the appropriate Python data type:
  - Name → `str`
  - Age → `int`
  - Height → `float`
  - Favourite number → `int`
- Displays each value, its data type, and its memory address.
- Calculates and displays an approximate birth year.
- Provides a clear, interactive command-line experience.

## Requirements

- Python 3.x
- A command-line terminal such as Command Prompt, PowerShell, or Terminal

## Project Files

| File | Description |
| --- | --- |
| `py1.py` | The main Python source code for the interactive data collector. |
| `op 1.py` | A saved sample output from a program run. |

## How It Works

When the program starts, it asks the user to enter the following information:

1. Name
2. Age
3. Height in metres
4. Favourite number

After receiving the inputs, the application displays each value with its Python data type and memory address. It then calculates the approximate birth year using the following formula:

```text
Approximate birth year = 2026 - age
```

## How to Run the Program

1. Download or save `py1.py` to a folder on your computer.
2. Open Command Prompt, PowerShell, or another terminal in that folder.
3. Run the following command:

```bash
python py1.py
```

4. Enter the requested details when prompted.
5. Review the displayed information and approximate birth year.

## Example

### Sample Input

```text
Name: Khushi
Age: 20
Height: 1.575
Favourite number: 22
```

### Sample Result

```text
Name: Khushi       Type: str
Age: 20            Type: int
Height: 1.575      Type: float
Favourite number: 22   Type: int

Approximate birth year: 2006
```

## Screenshot

The following image shows an example of the program running in a terminal. Memory addresses may be different every time the program runs and will vary between computers.

![Sample program output](<img width="1451" height="727" alt="output ss" src="https://github.com/user-attachments/assets/486af3c6-d09c-4bd1-afe5-938e87868432" />
)

## Demo Video

[Watch the project demonstration video]

(https://github.com/user-attachments/assets/54fba34a-cdde-4101-a6cf-84711455e2ad)

> Replace `YOUR_VIDEO_ID` with the ID of your uploaded YouTube video. For example, if your video link is `https://www.youtube.com/watch?v=abc123`, replace the placeholder with `abc123`.

## Concepts Used

| Concept | Purpose in This Project |
| --- | --- |
| `input()` | Collects information from the user. |
| `int()` | Converts age and favourite number inputs into integers. |
| `float()` | Converts height input into a decimal number. |
| `type()` | Displays the data type of each variable. |
| `id()` | Displays the memory address associated with each variable. |
| Arithmetic operators | Calculates the approximate year of birth. |

## Important Note

The birth year is an approximation because the calculation uses only the user's age. Depending on whether the user has already celebrated their birthday in the current year, the actual birth year may differ by one year.

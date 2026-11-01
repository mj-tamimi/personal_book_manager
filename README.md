# Personal Task Manager
A simple Personal Book Manager made with Python.

![Static Badge](https://img.shields.io/badge/Python-3.12%2B-blue)
![Static Badge](https://img.shields.io/badge/python-dotenv-red)


## Features
- Adds multiple Books
- Saves Books
- Loads Saved Books
- Active Admin Mode

## Project Structure
| File | Description |
|------|-------------|
| `main.py` |  Runs the main code. |
| `books.py` | Stores functions (defs). |
| `.gitignore` | Ignores unwanted files and folders. |
| `.env.example` | Used as a template for the user. |
| `requirements.txt` | To install every needed library in order to run the code. |
| `media/` | Stores the screenshots and gifs for the README file. |

## How it Works

- Progeam takes the name of the user.
- Asks user if they want admin mode.
- Assuming user says yes, the program will check the password from the `.env` file
- During the process, the program is also going to check the `books.json` file.
- Program asks user for the number of the books the user intends to add, and the book titles.
- All the books will be saved to `books.json`.


## Requirements
- `Python`
- `python-dotenv`

## Installation
Install the required packages:

```bash
python -m pip install -r requirements.txt
```
## Envoirement Setup
Create a `.env` file in the project folder.

Use `.env.example` as a template.

### Add your admin password

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```
Replace `your_password_here` with your own admin password.

## Troubleshoot
Possible errors you might get when running the file:

| Error | Explanation | 
|------|-------------|
| `python-dotenv` not found | Means `python-dotenv` is not on your computer, and you need to install it |
| FileNotFoundError | The program cannot find the `books.json` file. |
| JSONDecodeError | `books.json` file is empty or broken. |
| Password from `.env` | Mostly goes back to python-dotenv errors |
## Run the Program
Run the `main.py` file:
```bash
python main.py
```

## Screenshot
![personal_book_manager_screenshot](media/image.png)

## Demo
![personal_book_manager_demo](media/demo.gif)
# HSN Code Validator

A simple Python command-line tool that validates **HSN (Harmonized System of Nomenclature) codes** based on their numeric format and length.

## 📌 Features

- Checks whether the entered HSN code contains only numeric characters
- Validates the HSN code length
- Supports 4-digit, 6-digit, and 8-digit HSN codes
- Provides clear validation results through the command line

## 🛠️ Requirements

- Python 3.x
- Windows, macOS, or Linux

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/madhupriya8322/hsn-code-validator.git
cd hsn-code-validator
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Run the Program

```bash
python main.py
```

## 🧪 Example

### Valid HSN Code

```text
Enter an HSN code: 1234
✅ 1234 is a valid HSN code.
```

### Invalid HSN Code

```text
Enter an HSN code: 12ab
❌ 12ab is NOT a valid HSN code.
```

## ✅ Validation Rules

An HSN code is considered valid when:

- It contains only numeric characters
- Its length is **4, 6, or 8 digits**

| Input | Result |
|---|---|
| `1234` | ✅ Valid |
| `123456` | ✅ Valid |
| `12345678` | ✅ Valid |
| `12ab` | ❌ Invalid |
| `12345` | ❌ Invalid |

## 📂 Project Structure

```text
hsn-code-validator/
│
├── main.py
├── README.md
└── .gitignore
```

## 🎯 Purpose

This project demonstrates basic Python programming concepts, including:

- User input handling
- String validation
- Conditional statements
- Command-line applications

## 🔮 Future Improvements

- Add validation against an official HSN code database
- Add support for bulk HSN code validation
- Add a graphical user interface
- Add automated tests
- Provide more detailed validation messages

## 📄 License

This project is intended for personal and educational use.

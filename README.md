# DonationRegistryConsole
### Simple Donation Management System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Console](https://img.shields.io/badge/Type-Console%20App-orange)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-success)

A console-based donation tracking application that allows users to register, login, make donations, and view donation history.

## Screenshots

> **Note:** Console interface screenshots will be added soon. Run `python app.py` to see the donation system in action.

## Overview

This Python application demonstrates user authentication, session management, and basic CRUD operations in a console environment. Users can create accounts, log in securely, make monetary donations, and view all donations made by all users.

## Features

- **User Registration**: Create new user accounts with username/password
- **User Authentication**: Secure login system with session management
- **Donation Tracking**: Record and display monetary donations
- **Session Management**: Track currently logged-in user
- **Donation History**: View all donations made by all users

## Menu Options

1. **Login**: Authenticate with existing username/password
2. **Register**: Create a new user account
3. **Donate**: Make a donation (requires login)
4. **Show Donations**: View all donation records
5. **Exit**: Leave the application

## How to Run

```bash
python app.py
```

## Project Structure

```
DonationRegistryConsole/
├── app.py                 # Main application entry point
├── donations_pkg/         # Package for donation functionality
│   ├── __init__.py       # Package initializer
│   ├── homepage.py       # Menu display module
│   └── user.py           # User management and donation logic
└── README.md             # This file
```

## Technical Details

- **Language**: Python 3
- **Architecture**: Modular package structure
- **Data Storage**: In-memory (data lost on exit)
- **Authentication**: Simple username/password system
- **Default Account**: admin/password123

## Sample Usage

```
=== DonateMe Console ===
1. Login
2. Register
3. Donate
4. Show Donations
5. Exit

You must be logged in to donate

Choose an option: 1
Username: admin
Password: password123
Login successful!

Logged in as: admin

Choose an option: 3
Enter donation amount: $50
admin donated $50.00
```

## Security Note

⚠️ **This is a demonstration project.** In production environments:
- Passwords should be hashed (use `bcrypt` or `argon2`)
- User data should be stored in a secure database (PostgreSQL, MongoDB)
- Implement input sanitization to prevent injection attacks
- Use HTTPS for any network communication
- Add rate limiting for login attempts

## Prerequisites

- **Python**: version 3.6 or higher ([Download](https://www.python.org/downloads/))
- **No external dependencies** - uses only Python standard library

To check your Python version:
```bash
python --version
# or
python3 --version
```

## Troubleshooting

### Common Issues

**Issue:** `python: command not found`

**Solution:** Install Python 3 from [python.org](https://www.python.org/downloads/) or use `python3 app.py` instead.

---

**Issue:** "Must be logged in to donate" message persists after login

**Solution:** This indicates the login failed. Check your username/password. Default credentials: `admin` / `password123`

---

**Issue:** ModuleNotFoundError: No module named 'donations_pkg'

**Solution:** Ensure you're running the app from the project root directory where the `donations_pkg/` folder is located:
```bash
cd DonationRegistryConsole
python app.py
```

---

**Issue:** Donations disappear after exiting

**Solution:** This is expected behavior. The application uses in-memory storage. Data is lost when the program exits. For persistence, implement database storage.

---

**Issue:** Cannot register with existing username

**Solution:** Usernames must be unique. Choose a different username or login with the existing account.

For additional help, please open an issue in the repository issue tracker.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Enhancement Ideas
- Add password hashing for security
- Implement persistent storage (SQLite database)
- Add donation categories/causes
- Create user donation history (per user)
- Add donation statistics and reporting
- Implement admin panel for user management
- Add email notifications for donations
- Create GUI version with tkinter

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

- **Author**: José Santiago Echevarria
- **Issues**: Please report bugs via the repository issue tracker
- **Educational Context**: Demonstrates Python packages, user authentication, and session management
- **Security Warning**: Not for production use without implementing proper security measures

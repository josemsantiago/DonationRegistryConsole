# DonationRegistryConsole
### Simple Donation Management System

A console-based donation tracking application that allows users to register, login, make donations, and view donation history.

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

This is a demonstration project. In production, passwords should be hashed and user data should be stored persistently in a secure database.

## Requirements

- Python 3.x
- No external dependencies required

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

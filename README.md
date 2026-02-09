# AirBnB Clone - Command Interpreter

## Project Description
This project is the first step in building a full AirBnb clone web application.
The goal of the first stage is to create a **command-line interpreter** that manages the core objects of the application.

The command interpreter allows us to:
- Create new objects (ex, User, Place, State, City)
- Retrieve objects from storage
- Update existing objects
- Destroy objects
- Serialize and deserialize objects to and from JSON

This interpreter will be reused in later stages of the project such as database storage, RESTful API development, and front-end integration.

## Command Interpreter Description

The command interpreter is a shell-like program built using Python's `cmd` module.
It works in both **interactive mode** and **non-interactive mode**.

# Interactive mode 
```
$ ./console.py
(hbnb)
```

#Non-Interactive mode
`$echo "help" | ./console.y`


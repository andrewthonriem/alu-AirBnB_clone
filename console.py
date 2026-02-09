#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Mapping class names to actual classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone system."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl-D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and print its id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[arg]()
        storage.new(instance)
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = shlex.split(arg)
        all_objs = storage.all()
        if args:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            result = [str(obj) for k, obj in all_objs.items()
                      if k.startswith(args[0] + ".")]
        else:
            result = [str(obj) for obj in all_objs.values()]
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = all_objs[key]

        i = 2
        while i < len(args):
            attr_name = args[i]
            if i + 1 < len(args):
                attr_value = args[i + 1]

                # Cast value to int/float if possible
                try:
                    if "." in attr_value:
                        attr_value = float(attr_value)
                    elif attr_value.isdigit():
                        attr_value = int(attr_value)
                except Exception:
                    pass

                # Skip protected attributes
                if attr_name not in ("id", "created_at", "updated_at"):
                    setattr(obj, attr_name, attr_value)
            i += 2

        storage.save()

    def do_count(self, arg):
        """Count number of instances of a class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        count = sum(1 for key in storage.all()
                    if key.startswith(args[0] + "."))
        print(count)

    def parse_advanced_args(self, args):
        """Parse arguments inside parentheses for advanced commands."""
        args = args.strip()
        if not args:
            return []

        # Dictionary case: {"first_name": "Alice", "age": 30}
        if args.startswith("{") and args.endswith("}"):
            import ast
            try:
                dict_obj = ast.literal_eval(args)
                parts = []
                for k, v in dict_obj.items():
                    parts.append(str(k))
                    parts.append(str(v))
                return parts
            except Exception:
                return []

        # Normal case: "id", "attr", "value"
        try:
            return shlex.split(args)
        except Exception:
            return args.split() if args else []

    def default(self, line):
        """Handle advanced syntax: <class>.<command>(<args>)"""
        if "." in line and "(" in line and ")" in line:
            try:
                cls_name, rest = line.split(".", 1)
                command, args = rest.split("(", 1)
                args = args.rstrip(")")

                if cls_name not in classes:
                    print("** class doesn't exist **")
                    return

                args_list = self.parse_advanced_args(args)
                cleaned_args = [a.strip('"').strip("'") for a in args_list]

                method_name = f"do_{command}"
                if hasattr(self, method_name):
                    if cleaned_args:
                        arg_str = cls_name + " " + " ".join(cleaned_args)
                    else:
                        arg_str = cls_name
                    return getattr(self, method_name)(arg_str)
            except Exception:
                pass

        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
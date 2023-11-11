#!/usr/bin/python3
"""
This is the entry point for the AirBnB command interpreter.
"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program on EOF (Ctrl-D)
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel, save it, and print the id
        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Print the string representation of an instance based
        on class name and id
        Usage: show <class_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on class name and id
        (save the change into the JSON file)
        Usage: destroy <class_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print string representations of all instances or all instances
        of a specific class
        Usage: all [class_name]
        """
        args = line.split()
        if not args:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] not in models.classes.keys():
            print("** class doesn't exist **")
        else:
            instances = [
                str(value) for key, value in models.storage.all().items()
                if key.split('.')[0] == args[0]
                ]
            print(instances)

    def do_update(self, line):
        """
        Update an instance based on class name and id by adding or
        updating attribute
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                try:
                    setattr(models.storage.all()[key], args[2], eval(args[3]))
                    models.storage.all()[key].save()
                except Exception:
                    pass
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

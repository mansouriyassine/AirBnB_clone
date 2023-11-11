#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if arg in ["BaseModel", "User", "Place", "State", "City", "Amenity",
                   "Review"]:
            obj = globals()[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **" if arg else
                  "** class name missing **")

    def do_show(self, arg):
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not args else
                  "** instance id missing **")
            return
        if args[0] not in ["BaseModel", "User", "Place", "State", "City",
                           "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not args else
                  "** instance id missing **")
            return
        if args[0] not in ["BaseModel", "User", "Place", "State", "City",
                           "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        args = arg.split()
        if len(args) > 0 and args[0] not in ["BaseModel", "User", "Place",
                                             "State", "City", "Amenity",
                                             "Review"]:
            print("** class doesn't exist **")
            return
        obj_list = [
            str(obj) for obj in storage.all().values()
            if len(args) == 0 or args[0] == obj.__class__.__name__
        ]
        print(obj_list)

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 4:
            print("** class name missing **" if len(args) == 0 else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **" if len(args) == 2 else
                  "** value missing **")
            return
        if args[0] not in ["BaseModel", "User", "Place", "State", "City",
                           "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

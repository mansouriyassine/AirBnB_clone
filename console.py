#!/usr/bin/python3
import cmd
import shlex
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
    class_list = ["BaseModel", "User", "Place", "State", "City",
                  "Amenity", "Review"]

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def default(self, line):
        args = line.split('.')
        if len(args) == 2 and args[0] in self.class_list:
            cmd_args = args[1].split('(')[1].split(')')[0]
            if args[1][:3] == "all":
                self.do_all(args[0])
            elif args[1][:5] == "count":
                self.count_instances(args[0])
            elif args[1][:4] == "show":
                self.show_instance(args[0], cmd_args)
            elif args[1][:7] == "destroy":
                self.destroy_instance(args[0], cmd_args)
            elif args[1][:6] == "update":
                self.update_instance(args[0], *shlex.split(args[1][7:-1]))
            else:
                cmd.Cmd.default(self, line)
        else:
            cmd.Cmd.default(self, line)

    def do_create(self, arg):
        args = shlex.split(arg)
        if not args or args[0] not in self.class_list:
            print("** class name missing **" if not args else
                  "** class doesn't exist **")
        else:
            obj = globals()[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        self.show_instance(*shlex.split(arg))

    def do_destroy(self, arg):
        self.destroy_instance(*shlex.split(arg))

    def do_all(self, arg):
        args = shlex.split(arg)
        if args and args[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj_list = [str(obj) for obj in storage.all().values()
                        if not args or args[0] == obj.__class__.__name__]
            print(obj_list)

    def do_update(self, arg):
        self.update_instance(*shlex.split(arg))

    def count_instances(self, class_name):
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def show_instance(self, class_name, instance_id):
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def destroy_instance(self, class_name, instance_id):
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def update_instance(self, class_name, instance_id, *args):
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        elif not args:
            print("** attribute name missing **")
        elif len(args) == 1:
            print("** value missing **")
        elif len(args) == 2:
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                if args[0] not in ['id', 'created_at', 'updated_at']:
                    setattr(storage.all()[key], args[0], args[1])
                    storage.all()[key].save()
            else:
                print("** no instance found **")
        elif len(args) == 3 and isinstance(args[2], dict):
            for k, v in args[2].items():
                self.update_instance(class_name, instance_id, k, v)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

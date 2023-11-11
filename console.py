#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def do_help(self, arg):
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

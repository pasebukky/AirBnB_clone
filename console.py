#!/usr/bin/python3
""" This program contains the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ This class handles commands on the console """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command used to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command used to exit the program """
        return True

    def emptyline(self):
        """ Command to do nothing when an emptyline is encountered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" This program contains the entry point of the command interpreter """

import cmd
import models
import shlex
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = dict(BaseModel=BaseModel, User=User, State=State, City=City,
               Amenity=Amenity, Place=Place, Review=Review)
commands = ['create', 'show', 'update', 'all', 'destroy', 'count']


class HBNBCommand(cmd.Cmd):
    """ This class handles commands on the console """

    prompt = "(hbnb) "

    def precmd(self, line):
        """Parse command before passing to other methods"""
        if '.' in line and '(' in line and ')' in line:
            cls = line.split(".")[0]
            cmd = line.split('.')[1].split('(')[0]
            args_split = line.split('(')[1].split(')')[0]
            args_list = [arg.strip('"') for arg in args_split.split(',')]
            args_list = [arg.replace('"', "").strip() for arg in args_list]
            if cls in classes and cmd in commands:
                line = cmd + ' ' + cls + ' ' + ' '.join(args_list)
        return line

    def do_quit(self, line):
        """ Quit command used to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command used to exit the program """
        return True

    def emptyline(self):
        """ Command to do nothing when an emptyline is encountered """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it & prints the id """
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                instance_key = classes[class_name]()
                instance_key.save()
                print(instance_key.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                objs = models.storage.all()
                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key not in objs:
                    print("** no instance found **")
                else:
                    print(objs[instance_key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                objs = models.storage.all()
                instance_key = "{}.{}".format(class_name, instance_id)
                if instance_key not in objs:
                    print("** no instance found **")
                else:
                    del models.storage.all()[instance_key]
                    models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        instance_list = []
        if not line:
            # Add instance to the list without printing individually
            instance_list.extend(str(instance) for instance in
                                 models.storage.all().values())
        else:
            args = line.split()
            class_name = args[0]
            if class_name in classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == class_name:
                        instance_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(instance_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
         Args:
            line (line): command line arg
            usage:  update <class> <id> <attribute_name> <attribute_value>
                <class>.update(<id>, <attribute_name>, <attribute_value>)
                <class>.update(<id>, <dictionary>)
        """

        all_objs = storage.all()
        line_split = shlex.split(line)
        len_line = len(line_split)

        if len_line < 1:
            print("** class name missing **")
            return False
        else:
            cls = line_split[0]
            if (cls not in classes):
                print("** class doesn't exist **")
                return False
            else:
                try:
                    cls_id = line_split[1]
                    key = cls + "." + cls_id
                    try:
                        unused = all_objs[key]
                    except KeyError:
                        print("** no instance found **")
                        return False
                except IndexError:
                    print('** instance id missing **')
                    return False
                if len_line < 3:
                    print("** attribute name missing **")
                    return False
                elif len_line < 4:
                    print("** value missing **")
                    return False

        key = cls + "." + cls_id
        if len_line > 2:
            if len_line > 3:
                setattr(storage.all()[key], line_split[2], line_split[3])
                storage.all()[key].save()
            else:
                return

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        pass

    def do_count(self, args):
        """Count instances of class"""
        count = 0
        all_objs = storage.all()
        for key in all_objs.keys():
            key_split = key.split(".")
            key_cls = key_split[0]
            if key_cls == args:
                count = count + 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

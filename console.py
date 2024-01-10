#!/usr/bin/python3
""" This program contains the entry point of the command interpreter """

import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = dict(BaseModel=BaseModel, User=User, State=State, City=City,
               Amenity=Amenity, Place=Place, Review=Review)


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

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it & prints the id """
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                instance_key = BaseModel()
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
        args = line.split()
        if len(args) == 0:
            objs = storage.find.all()
            print([str(obj) for obj in objs])
        elif len(args) == 1:
            class_name = args[0]
            try:
                objs = storage.find_all(class_name)
                print([str(obj) for obj in objs])
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            pass

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file
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
                instance_key = "{}.{}".format(class_name, instance_id)
                objs = models.storage.all()
                if instance_key not in objs:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[instance_key],
                            attribute_name, attribute_value)
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

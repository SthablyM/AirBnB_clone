#!/usr/bin/python3
"""Define  the HBNB console"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define the HBNB Command"""
    prompt = '(hbnb) '
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("Quit command to exit the program")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = arg.strip()
                instance = globals()[class_name]()
                instance.save()
                print(instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = arg.split()
        if len(args) != 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = class_name + "." + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self,arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class doesn't exist **")
            return

        args = arg.split()
        class_name = arg[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) > 2:
            print("** instance id missing **")
            return

        instances = BaseModel.load()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        BaseModel.save(instances)


    def do_all(self,arg):
        """print the string representing of an instance"""
        args = arg.split()

        if len(args) == 0:
            instances = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            instances = [obj for obj in storage.all().values() if type(obj).__name__ == class_name]
        print("Instances:", instances)
        print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 4:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        attribute_name = args[2]
        attribute_name = args[3]

        instance = storage.all()[key]
        if hasattr(instance, attribute_name):
            if attribute_name in ["id", "created_at", "updated_at"]:
                print("** can't update id, created_at, or updated_at **")
                return
            attribute_type = type(getattr(instance, attribute_name))

            try:
                if attribute_type == int:
                    attribute_value = int(attribute_value)
                elif attribute_type == float:
                    attribute_value = float(attribute_value)

            except ValueError:
                pass
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** attribute name doesn't exist **")



if __name__ == '__main__':
      HBNBCommand().cmdloop()


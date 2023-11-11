# file_storage.py
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {
            k: v.to_dict() for k, v in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for k, v in objects.items():
                class_name = v['__class__']
                if class_name == 'User':
                    FileStorage.__objects[k] = User(**v)
                elif class_name == 'BaseModel':
                    FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass

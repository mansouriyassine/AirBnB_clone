#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for k, v in objects.items():
                cls_name = v['__class__']
                from models.base_model import BaseModel
                cls = eval(cls_name)
                FileStorage.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass

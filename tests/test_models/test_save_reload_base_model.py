#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel


class TestSaveReloadBaseModel(unittest.TestCase):

    def test_save_reload(self):
        """Test saving and reloading a BaseModel instance"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()

        # Retrieve all objects from storage
        all_objs = storage.all()
        self.assertIn(f"BaseModel.{my_model.id}", all_objs)

        retrieved_model = all_objs[f"BaseModel.{my_model.id}"]
        self.assertEqual(retrieved_model.name, "My First Model")
        self.assertEqual(retrieved_model.my_number, 89)

    def test_persistence(self):
        """Test the persistence of objects in the file storage"""
        my_model = BaseModel()
        my_model.save()

        storage.reload()
        all_objs = storage.all()
        self.assertIn(f"BaseModel.{my_model.id}", all_objs)


if __name__ == "__main__":
    unittest.main()

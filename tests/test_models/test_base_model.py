#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_id_creation(self):
        """Test if id is created and its type"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertIsInstance(model.id, str)

    def test_id_uniqueness(self):
        """Test if different instances have unique ids"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_datetime_creation(self):
        """Test if created_at and updated_at are created"""
        model = BaseModel()
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), expected_str)

    def test_save_method(self):
        """Test if save method updates updated_at attribute"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    # Add more tests as needed...

if __name__ == "__main__":
    unittest.main()

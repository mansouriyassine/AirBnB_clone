#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    
    def test_create_from_dict(self):
        """Test creation of BaseModel from dictionary"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.name, "My_First_Model")
        self.assertEqual(my_new_model.my_number, 89)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)
        self.assertNotEqual(my_new_model, my_model)

    def test_create_from_empty_dict(self):
        """Test creation of BaseModel with empty dict"""
        my_model = BaseModel(**{})
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

import os
import models
import json 
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):
    """Unittest  testing of the Filestorage"""
    def test_all_storage(self):
        """Test all () method return dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self, obj):
        """Test method by sorting objects"""
        with self.assertRaises(AttributeError):
            models.storage.new(obj)

    def test_new(self):
        """Test creating  a new object"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        """Test a saving object to a file"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload(self):
        """Test a reload of a file """
        with self.assertRaises(TypeError):
            obj = BaseModel()
            models.storage.new(BaseModel(), 1)
        
            new_storage = FileStorage
            new_storage.reload()

class TestFileStorage_Instatiation(unittest.TestCase):
    """Unittest testing of the instatiation of the class Filestorage"""
    def test_FileStorage_insta_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_insta_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    
if __name__ == '__main__':
    unittest.main()

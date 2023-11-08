
import os
import shutil
import unittest
from CPCReady.func_project import create
import io
from unittest.mock import patch


class TestCPCReady(unittest.TestCase):

    def setUp(self):
        self.test_project_path = os.getcwd() + '/test/data'
        os.makedirs(self.test_project_path, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_project_path + "/project2")

    @patch('inquirer.prompt', return_value={'nomenclatura': 'Yes', 'project_name': 'project2'})
    def test_create_project(self, mock_prompt):
        os.chdir(self.test_project_path)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            create()
            output = mock_stdout.getvalue()
        self.assertIn("Thank you for using CPCReady", output)


if __name__ == '__main__':
    unittest.main()

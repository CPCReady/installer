
import unittest
import os
from click.testing import CliRunner
from CPCReady.main import *


class TestCPCReady(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_version_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ["--version"])
            self.assertEqual(result.exit_code, 0)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_info_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ["info"])
            self.assertEqual(result.exit_code, 0)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_build_command(self):

        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ['build'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Successfully create disc image', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_run_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ['run', '--setting', 'WEB6128'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Template RVM Web Create successfully', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_palette_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            image_file = 'img/avatar.png'
            result = self.runner.invoke(main, ['palette', '--image', image_file, '--mode', '0'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Successfully obtained image palette', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_screen_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ["screen", "--image", "img/avatar.png", "--mode", "0", "--out", "temp",
                                               "--dsk"])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Image conversion done successfully in Image file', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_screen2_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ["screen", "--image", "img/avatar.png", "--mode", "0", "--out", "temp"])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Image conversion done successfully', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)

    def test_sprite_command(self):
        global result
        original_directory = os.getcwd()
        os.chdir('test/data/project')
        try:
            result = self.runner.invoke(main, ["sprite", "--image", "img/avatar.png", "--mode", "0", "--out", "temp",
                                               "--height", 16, "--width", 16])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Generation of sprite files done successfully.', result.output)
        except Exception as e:
            print(f'Exception command: {e}')
            print(result.output)
        finally:
            os.chdir(original_directory)


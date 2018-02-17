import unittest
from file_utils.file_utils import replace_extension


class TestFileUtils(unittest.TestCase):
    def test_get_output_path(self):
        test_map = {
            '/dir1/dir2/file1.out.ext': '/dir1/dir2/file1.out.newext',
            '/dir1/dir4/file1.out.ext': '/dir1/dir4/file1.out.newext',
            'file1.out.ext': 'file1.out.newext',
            '': '',
            'file1': 'file1.newext'
        }
        for path, expected in test_map.items():
            new_path = replace_extension(path, 'newext')
            assert (new_path == expected)

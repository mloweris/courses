import subprocess
import unittest

def test_grade(file_arg):
    cmd = ['python', '../../28/add_grader.py', file_arg]
    return subprocess.check_output(cmd).strip()

class SentGraderTests(unittest.TestCase):

    def test_success(self):
        op = test_grade('test_success.db')
        self.assertEqual(op, '1;Good Job!')

    def test_fail(self):
        op = test_grade('test_fail.db')
        self.assertEqual(op, '0;Expected 126 at (0,0), got: 120')


if __name__ == '__main__':
    unittest.main()

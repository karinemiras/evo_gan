import unittest

from presenter.logger import Logger


class TestStringMethods(unittest.TestCase):

    def test_user_input(self):
        logger = Logger()

        logger.open_log(template=True)

        self.assertEqual(len(logger.generations_data['generations']), 2)


if __name__ == '__main__':
    unittest.main()
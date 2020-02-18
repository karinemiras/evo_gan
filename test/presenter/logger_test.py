import unittest

from presenter.logger import Logger


class TestLoggerMethods(unittest.TestCase):

    def test_logger(self):
        logger = Logger()

        logger.open_log(template=True)

        self.assertEqual(len(logger.generations_data['generations']), logger.generation.index)


if __name__ == '__main__':
    unittest.main()
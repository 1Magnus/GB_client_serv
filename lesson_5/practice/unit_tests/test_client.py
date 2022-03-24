import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT
from client import create_presence, process_ans, check_commond_argv


class TestClass(unittest.TestCase):
    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        r = process_ans({RESPONSE: 200})
        self.assertEqual(r, '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        r = process_ans({RESPONSE: 400, ERROR: 'Bad Request'})
        self.assertEqual(r, '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

    def test_noargv(self):
        """Тест отсутствия параметров командной строки"""
        server_address, server_port = check_commond_argv()
        r = [server_address, server_port]
        self.assertEqual(r, [DEFAULT_IP_ADDRESS, DEFAULT_PORT])


if __name__ == '__main__':
    unittest.main()

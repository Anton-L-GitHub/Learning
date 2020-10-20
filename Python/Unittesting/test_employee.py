import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Carl', 'Larsson', 50000)
        self.emp_2 = Employee('Pelle', 'Persson', 60000)

    def tearDown(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Carl Larsson')
        self.assertEqual(self.emp_2.fullname, 'Pelle Persson')

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Carl.Larsson@email.com')
        self.assertEqual(self.emp_2.email, 'Pelle.Persson@email.com')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        ''' When you want to test things that you cant controll, in this exaple you test your code against a website, but the website can be down, but your code is fine. Then you can use mocking.'''
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Larsson/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Persson/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()

import unittest

__author__ = 'elip'


class TestPlugin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass  # this is the place for class scoped initialization

    @classmethod
    def tearDownClass(cls):
        pass  # this is the place for class scoped cleanup

    def test_my_task(self):  # test methods should start with the word 'test'

        from plugin.tasks import my_task
        my_task()

        ###################
        # Asserts go here #
        ###################




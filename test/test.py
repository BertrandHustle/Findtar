import unittest
import findtar

test_array = ['/var/spool/cron', '/var/log/cron', '/opt/google/talkplugin/cron']
test_selection = '1,3-4'


class FindTarTests(unittest.TestCase):

    # Given an array of find results and a selection of those results
    # When selection is applied to array
    # Then correct selection of elements from array is returned

    def test_select_from_array(self):

        # arrange
        expected_result = '/var/spool/cron /opt/google/talkplugin/cron '

        # act
        test_select = findtar.select_from_array(test_array, test_selection)

        # assert
        self.assertEqual(test_select, expected_result)

    # Given a selection consisting of a single number
    # When selection is applied to array
    # Then single file name from array is returned

    def test_single_number_selection(self):

        # arrange
        expected_result = '/var/log/cron '
        single_test_selection = '2'

        # act
        test_select = findtar.select_from_array(test_array, single_test_selection)

        # assert
        self.assertEqual(test_select, expected_result)


if __name__ == '__main__':
    unittest.main()

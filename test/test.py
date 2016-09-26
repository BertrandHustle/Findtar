import unittest
import findtar

test_array = ['/var/spool/cron', '/var/log/cron', '/opt/google/talkplugin/cron']
test_array2 = ['B', 'X', 'Y', 'G', 'W', 'E', 'M', 'A', 'K', 'P']
test_selection = '1,3-4'
test_selection2 = '1,5,6-10'


class FindTarTests(unittest.TestCase):

    # Given an array of find results and a selection of those results
    # When selection is applied to array
    # Then correct selection of elements from array is returned

    def test_select_from_array(self):

        # arrange
        expected_result = 'B W E M A K P '

        # act
        test_select = findtar.select_from_array(test_array2, test_selection2)

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

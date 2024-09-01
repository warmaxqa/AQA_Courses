import unittest
from unittest.mock import patch
from function_log_event import log_event

class TestLogEvent(unittest.TestCase):

    @patch('logging.info')
    def test_log_event_success(self, mock_info):
        # test succesfully enter
        log_event('test_user', 'success')
        mock_info.assert_called_once_with("User 'test_user' logged in successfully.")

    @patch('logging.warning')
    def test_log_event_expired(self, mock_warning):
        # test old password
        log_event('test_user', 'expired')
        mock_warning.assert_called_once_with("User 'test_user' password expired, needs to change.")

    @patch('logging.error')
    def test_log_event_failed(self, mock_error):
        # test failed enter
        log_event('test_user', 'failed')
        mock_error.assert_called_once_with("User 'test_user' failed to log in due to incorrect password.")

    def test_log_event_invalid_status(self):
        # tet invalid status
        with self.assertRaises(ValueError):
            log_event('test_user', 'invalid_status')

if __name__ == '__main__':
    unittest.main()
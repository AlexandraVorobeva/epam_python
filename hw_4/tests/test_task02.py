from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from hw_4.task_2_mock_input import count_dots_on_i

import pytest


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_urlopen):
    my_mock = MagicMock()
    my_mock.read.return_value = b"i i i i i"
    mock_urlopen.return_value = my_mock
    res = count_dots_on_i(my_mock)
    assert res == 5


@patch("urllib.request.urlopen")
def test_unreachable_url(mock_urlopen):
    my_mock = MagicMock()
    mock_urlopen.side_effect = HTTPError(
        "http://example.com", 500, "Internal Error", {}, None
    )
    with pytest.raises(ValueError, match="Unreachable {url}"):
        count_dots_on_i(my_mock)

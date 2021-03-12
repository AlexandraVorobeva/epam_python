from typing import Any, Dict, List

import pytest

from hw_3.task03.task03 import make_filter


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "name": "polly",
        "type": "bird",
    },
]


@pytest.mark.parametrize(
    "params, data, expected_result ",
    [
        ({"name": "404", "type": "error"}, sample_data, []),
        ({"name": "Bill", "occupation": "was here"}, sample_data, [sample_data[0]]),
        ({"name": "polly", "type": "bird"}, sample_data, [sample_data[1]]),
    ],
)
def test_make_filter(
    params: Dict[Any, Any], data: List[Any], expected_result: List[Any]
):
    assert make_filter(**params).apply(data) == expected_result
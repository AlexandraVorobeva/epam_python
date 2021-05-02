from hw_9.hw1 import merge_sorted_files


def test_merge_sorted_files_two_files():
    actual_result = list(merge_sorted_files(["file_1.txt", "file_2.txt"]))
    expected_result = [1, 2, 3, 4, 5, 6]
    assert actual_result == expected_result


def test_merge_sorted_files_one_file():
    actual_result = list(merge_sorted_files(["file_1.txt"]))
    expected_result = [4, 5, 6]
    assert actual_result == expected_result


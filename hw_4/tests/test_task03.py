import pytest

from hw_4.task_3_get_print_output import my_precious_logger


@pytest.mark.parametrize(
    "string_to_log",
    [
        "OK",
        "error: file not found",
        "error: expected a string for argument",
        "error: too many arguments",
    ],
)
def test_my_precious_logger(capsys, string_to_log: str):
    if string_to_log.startswith("error:"):
        my_precious_logger(string_to_log)

        assert capsys.readouterr().err == string_to_log
        assert capsys.readouterr().out != string_to_log
    else:
        my_precious_logger(string_to_log)

        assert capsys.readouterr().out == string_to_log
        assert capsys.readouterr().err != string_to_log
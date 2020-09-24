import constants

import os


def get_expected_problem_filepath():
    cwd = os.getcwd()
    expected_path = f'{cwd}/{constants.CODINGBAT_FILENAME}'
    return expected_path

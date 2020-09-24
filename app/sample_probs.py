from fetch_problems import main as fetch_probs_main
import utils

import argparse
import os
import random
import sys


def generate_sample(num_problems):
    expected_path = utils.get_expected_problem_filepath()
    if not os.path.exists(expected_path):
        # if the file containing sample problems does not yet exist,
        # attempt to create it.
        fetch_probs_main()

    with open(expected_path, 'r') as fl:
        problem_urls = fl.readlines()
        random.shuffle(problem_urls)
        problem_url_strings = ''.join(problem_urls[:num_problems])
        print(problem_url_strings)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Randomly suggest some CodingBat Python exercises to stay sharp with."
    )
    parser.add_argument(
        '--num_problems', 
        action='store',
        type=int, 
        default=5, 
    )
    args = parser.parse_args()
    generate_sample(num_problems=args.num_problems)

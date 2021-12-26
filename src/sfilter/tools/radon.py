"""
Call radon mi() command
"""
import logging

import radon.cli as cli


def run_radon(dir_path):
    logging.info("Start radon execution")
    cli.mi(paths=[dir_path], json=True, output_file="radon.json")
    logging.info("Finish radon execution")

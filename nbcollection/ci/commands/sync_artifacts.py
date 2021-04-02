import argparse
import os
import sys

from nbcollection.ci.commands.datatypes import CIMode, Site
from nbcollection.ci.commands.utils import validate_and_parse_inputs
from nbcollection.ci.constants import PROJECT_DIR
from nbcollection.ci.sync_artifacts.factory import run_sync

DESCRIPTION = "Build CI Configs for CircleCI, Github Actions, or others"
EXAMPLE_USAGE = """Example Usage:

    Generate .circleci/config.yaml environment
    nbcollection-ci sync-artifacts --collection-names jdat_notebooks

    Source Example:
    PYTHONPATH='.' python -m nbcollection.ci sync-artifacts --collection-names jdat_notebooks
"""


def convert(options=None):
    options = options or sys.argv

    parser = argparse.ArgumentParser(
            prog='nbcollection-ci merge-artifacts',
            description=DESCRIPTION,
            epilog=EXAMPLE_USAGE,
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-c', '--collection-names', required=False, default=None,
                        help="Select a subset of Collections to be built, or all will be built")
    parser.add_argument('-t', '--category-names', required=False, default=None,
                        help="Select a subset of Categories to be built, or all will be built")
    parser.add_argument('-n', '--notebook-names', required=False, default=None,
                        help="Select a subset of Notebooks to be built, or all will be built")
    parser.add_argument('-p', '--project-path', default=PROJECT_DIR, type=str,
                        help="Path relative to Project DIR install")
    parser.add_argument('-b', '--publish-branch', type=str, default='offline-artifacts')
    parser.add_argument('-r', '--publish-remote', type=str, default='origin')
    parser.add_argument('-s', '--site', type=Site, default=Site.GithubPages)
    parser.add_argument('-a', '--artifact-storage-directory', type=str, default='artifacts')

    options = parser.parse_args(options[2:])
    validate_and_parse_inputs(options)
    run_sync(options)

"""This module provides the CLI for tree builder"""
import argparse
import pathlib
import sys


from . import __version__
from .tree_builder import DirectoryTree


def main():
    args = parse_cmd_line_args()
    root_dir = pathlib.Path(args.root_dir)

    if not root_dir.is_dir():
        print("The specified root directory doesn't exist.")
        sys.exit(1)

    tree = DirectoryTree(
        root_dir=root_dir,
        dir_only=args.dir_only,
        output_file=args.output_file,
        sort_file_first=args.sort_file_first
    )
    tree.generate()


def parse_cmd_line_args():
    parser = argparse.ArgumentParser(
        prog="custom_tree",
        description="Tree, a directory tree generator",
        epilog=""
    )
    parser.version = f"Tree v{__version__}"

    # add positional and optional arguments to support
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree from the mentioned ROOT_DIR"
    )

    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree"
    )

    parser.add_argument(
        "-o",
        "--output-file",
        metavar="FILE_NAME",
        nargs="?",
        default=sys.stdout,
        help="save directory tree to the [FILE_NAME]"
    )

    parser.add_argument(
        "-s",
        "--sort-file-first",
        action="store_false",
        help="Display directory tree with files sorted first"
    )

    return parser.parse_args()

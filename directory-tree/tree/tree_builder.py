"""This module provides tree builder main module."""

import os
import pathlib
import sys

PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:

    def __init__(self, root_dir: str, dir_only: bool = False, output_file=sys.stdout, sort_file_first: bool = False) -> None:
        # colorama.init()
        self._output_file = output_file
        self._generator = _TreeGenerator(
            root_dir, dir_only=dir_only, sort_file_first=sort_file_first)

    def generate(self) -> None:
        tree = self._generator.build_tree()
        if self._output_file != sys.stdout:
            tree.insert(0, "```")
            tree.append("```")
            self._output_file = open(self._output_file, "w", encoding="UTF-8")

        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)


class _TreeGenerator:

    def __init__(self, root_dir: str, dir_only: bool = False, sort_file_first: bool = False) -> None:
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._sort_file_first = sort_file_first
        self._tree = []

    def build_tree(self) -> list:
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self) -> None:
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _prepare_entries(self, directory: pathlib.Path) -> list:
        if self._dir_only:
            entries = [x for x in directory.iterdir() if x.is_dir()]
            return entries
        entries = [x for x in directory.iterdir()]
        entries = sorted(entries, key=lambda entry: entry.is_file(
        ) if self._sort_file_first else not entry.is_file())
        return entries

    def _tree_body(self, directory: pathlib.Path, prefix: str = "") -> None:
        entries = self._prepare_entries(directory)
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = TEE if index != entries_count-1 else ELBOW
            if entry.is_dir():
                self._add_directory(
                    entry, index, entries_count, prefix, connector)
            else:
                self._add_file(entry, prefix, connector)

    def _add_directory(self, directory: pathlib.Path,  index: int, entries_count: int, prefix: str, connector: str):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix)
        if not self._dir_only:
            self._tree.append(prefix.rstrip())

    def _add_file(self, file: pathlib.Path, prefix, connector) -> None:
        self._tree.append(
            f"{prefix}{connector} {file.name}")

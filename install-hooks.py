#!/usr/bin/env python
import os
import pathlib
import shutil
import subprocess

hooks_git_project = "git@gitlab.dev.cit.io:citio/dev/install-hooks.git"
hooks_dir = "git_hooks"


def print_error_message(error: str) -> None:
    style_str = lambda style, s: f"\033[{style}m{s}\033[0m"

    msg = f"""
{style_str("31;1","ERROR")}
{style_str("1", error)}
"""
    print(msg)


def pull_project(path: pathlib.Path):
    pull_project = subprocess.Popen(
        f"git -C {path} pull origin master", shell=True, stderr=subprocess.PIPE
    )

    stdout, err = pull_project.communicate()
    if pull_project.returncode != 0:
        print_error_message(err.decode("utf-8").rstrip())
        os._exit(1)


def clone_project(path: pathlib.Path):
    clone_project = subprocess.Popen(
        f"git clone {hooks_git_project} {path}", shell=True, stderr=subprocess.PIPE
    )
    stdout, err = clone_project.communicate()
    if clone_project.returncode != 0:
        print_error_message(err.decode("utf-8").rstrip())
        os._exit(1)


def hooks_project_check_and_install(git_root: str) -> pathlib.Path:
    hooks_path = pathlib.Path(f"{git_root}{hooks_dir}")

    if hooks_path.exists():
        path_git_project = (
            subprocess.check_output(f"git -C {hooks_path} remote get-url origin", shell=True)
            .decode("utf-8")
            .rstrip()
        )

        if path_git_project == hooks_git_project:
            pull_project(hooks_path)
            return hooks_path
        else:
            shutil.rmtree(hooks_path)

    clone_project(hooks_path)
    return hooks_path


def load_hooks(path: pathlib.Path) -> None:
    load_hooks = subprocess.call(f"{path}/load_hooks.sh", shell=True)


if __name__ == "__main__":
    git_root = (
        subprocess.check_output("git rev-parse --show-cdup", shell=True).decode("utf-8").rstrip()
    )

    hooks_path = hooks_project_check_and_install(git_root)
    load_hooks(hooks_path)

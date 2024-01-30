"""
Invoke - Tasks
==============
"""

from invoke import task

__author__ = "Colour Developers"
__copyright__ = "Copyright 2018 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "precommit",
    "build",
    "release",
]


@task
def precommit(ctx):
    """
    Run the "pre-commit" hooks on the codebase.

    Parameters
    ----------
    ctx
        Context.
    """

    print('Running "pre-commit" hooks on the codebase...')  # noqa: T201
    ctx.run("pre-commit run --all-files")


@task(precommit)
def build(ctx):
    """
    Build the project.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    """

    print("Building...")  # noqa: T201
    ctx.run("cp readme.md docs/index.md")
    ctx.run("mkdocs build")


@task(build)
def release(ctx):
    """
    Release the project to *Github Pages*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    """

    print("Releasing...")  # noqa: T201

    output = ctx.run("git status")
    if "nothing to commit, working tree clean" not in output.stdout:
        raise RuntimeError("Working tree is not clean, please commit your changes!")

    ctx.run("mkdocs gh-deploy")

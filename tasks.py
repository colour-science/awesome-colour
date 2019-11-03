# -*- coding: utf-8 -*-
"""
Invoke - Tasks
==============
"""

from __future__ import unicode_literals

from invoke import task

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['formatting', 'quality', 'build', 'release']


@task
def formatting(ctx, yapf=True):
    """
    Formats the codebase with *Yapf*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    yapf : bool, optional
        Whether to format the codebase with *Yapf*.

    Returns
    -------
    bool
        Task success.
    """

    if yapf:
        print('Formatting codebase with "Yapf"...')
        ctx.run('yapf -p -i -r --exclude \'.git\' .')


@task
def quality(ctx, flake8=True):
    """
    Checks the codebase with *Flake8* and lints various *restructuredText*
    files with *rst-lint*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.
    flake8 : bool, optional
        Whether to check the codebase with *Flake8*.

    Returns
    -------
    bool
        Task success.
    """

    if flake8:
        print('Checking codebase with "Flake8"...')
        ctx.run('flake8')


@task(formatting, quality)
def build(ctx):
    """
    Builds the project.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    print('Building...')
    ctx.run('cp readme.md docs/index.md')
    ctx.run('mkdocs build')


@task(build)
def release(ctx):
    """
    Releases the project to *Github Pages*.

    Parameters
    ----------
    ctx : invoke.context.Context
        Context.

    Returns
    -------
    bool
        Task success.
    """

    print('Releasing...')

    output = ctx.run('git status')
    assert 'nothing to commit, working tree clean' in output.stdout, (
        'Working tree is not clean, please commit your changes!')

    ctx.run('mkdocs gh-deploy')

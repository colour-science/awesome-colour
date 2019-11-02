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

__all__ = ['build', 'release']


@task()
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

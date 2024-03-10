pipu - a pip clone that doesn't force you to use virtualenvs
============================================================

This is just a placeholder page, to show what a Pipu page and package would
look like.

The problem
-----------

The draft came about from `discussions over at Homebrew
<https://github.com/orgs/Homebrew/discussions/3404#discussioncomment-8737053>`_

The problem that Pipu may address, is that a `new standard
<https://peps.python.org/pep-0668/>`_ currently being rolled out will make
various standard distributions very difficult to use for beginners.  Here's an
example.  Let's say I install Homebrew Python 3.12, that does have this
standard installed.    I'm a beginner, interested in Python game programming,
and I found `this tutorial
<https://realpython.com/pygame-a-primer/#background-and-setup>`_.

It says that I need to install `pygame` with::

    pip install pygame

I run that, and I see this::

    error: externally-managed-environment

    × This environment is externally managed
    ╰─> To install Python packages system-wide, try brew install
        xyz, where xyz is the package you are trying to
        install.

        If you wish to install a non-brew-packaged Python package, create a
        virtual environment using python3 -m venv path/to/venv.  Then use
        path/to/venv/bin/python and path/to/venv/bin/pip.

        If you wish to install a non-brew packaged Python application, it may
        be easiest to use pipx install xyz, which will manage a virtual
        environment for you. Make sure you have pipx installed.

    note: If you believe this is a mistake, please contact your Python
    installation or OS distribution provider. You can override this, at the
    risk of breaking your Python installation or OS, by passing
    --break-system-packages.  hint: See PEP 668 for the detailed
    specification.

Remember, I'm a beginner.  So I guess I try::

    $ brew install pygame
    ==> Downloading https://formulae.brew.sh/api/formula.jws.json
    #=#=#                                                                          
    ==> Downloading https://formulae.brew.sh/api/cask.jws.json
    #=#=#                                                                          
    Warning: No available formula with the name "pygame". Did you mean pygments?
    ==> Searching for similarly named formulae and casks...
    ==> Formulae
    pygments

    To install pygments, run:
    brew install pygments

Maybe I do a bit of Googling, and work out that maybe I want::

    $ brew install python-pygame
    Warning: No available formula with the name "python-pygame". Did you mean python-pytz?
    ==> Searching for similarly named formulae and casks...
    ==> Formulae
    python-pytz

    To install python-pytz, run:
    brew install python-pytz

Now I'm a bit confused, and I go back to the original message.  This is the
next suggestion, but it looks very confusing, as I have no idea what a
virtualenv is::

        If you wish to install a non-brew-packaged Python package, create a
        virtual environment using python3 -m venv path/to/venv.  Then use
        path/to/venv/bin/python and path/to/venv/bin/pip.

Presumably I would have given up on Homebrew by now, but let's say I'm brave,
and I do eventually work out that I can do this::

    python3 -m venv path/to/venv
    path/to/venv/bin/pip install pygame

But I still really need to know what this virtualenv thing is, that I will
have to always run `path/to/venv/bin/python3` to get an interactive console in
which I can import `pygame`, I'll have to remember where these files are in my
``$PATH`` (which is not always easy for beginners) and so on.

Ok, but now I want to use `ipython` or `jupyter`.  If I've developed some
understanding by now, then I might realize I need to do::

    path/to/venv/bin/pip install ipython

but now I have to work out that my next step is::

    path/to/venv/bin/ipython

In short, I'll have to understand what virtualenvs are and how they work.

More plausibly, the instructions on virtualenvs above look so confusing, that
I try the next instructions::

        If you wish to install a non-brew packaged Python application, it may
        be easiest to use pipx install xyz, which will manage a virtual
        environment for you. Make sure you have pipx installed.

OK, I work out that I first need::

    brew install pipx

Then::

    pipx install pygame

I get::

    $ pipx install pygame
    No apps associated with package pygame or its dependencies. If you are
    attempting to install a library, pipx should not be used. Consider using
    pip or a similar tool instead.

OK - so I'm left with this final note::

    note: If you believe this is a mistake, please contact your Python
    installation or OS distribution provider. You can override this, at the
    risk of breaking your Python installation or OS, by passing
    --break-system-packages.  hint: See PEP 668 for the detailed
    specification.

That sounds far too scary - I mean - they wouldn't give me that warning if
they weren't serious.   So I conclude Homebrew is not for me and I install
something else.  Probably Conda.

Maybe a solution
----------------

The plan for Pipu is that it be a drop in replacement for Pip - the Python
Package Installer.

It will be designed to act exactly as Pip does with a single exception - it
will not try and force you into using virtualenvs if you are working on a
Python distribution like Homebrew or Gentoo.

See the `Pip documentation <https://pip.matthew-brett.io>`_ for usage and
other instructions.   To use `pipu` just use `pipu` instead of `pip`
throughout.

We will release updates regularly, with a new version every 3 months, closely
following Pip's own release schedule.

If you have an issue with Pipu, please first try:

* `Issue tracking`_

If you want to get involved, head over to GitHub to get the source code.

* `GitHub page`_

.. _Python Package Index: https://pypi.org
.. _GitHub page: https://github.com/matthew-brett/pipu
.. _Development documentation: https://matthew-brett.github.io/pipu
.. _Issue tracking: https://github.com/matthew-brett/pipu/issues

from typing import Iterator

import pytest

from pipu._internal.cli.req_command import RequirementCommand
from pipu._internal.commands.install import InstallCommand
from pipu._internal.index.collector import LinkCollector
from pipu._internal.index.package_finder import PackageFinder

# from pipu._internal.models.index import PyPI
from pipu._internal.models.search_scope import SearchScope
from pipu._internal.models.selection_prefs import SelectionPreferences
from pipu._internal.network.session import PipSession
from pipu._internal.operations.build.build_tracker import get_build_tracker
from pipu._internal.operations.prepare import RequirementPreparer
from pipu._internal.req.constructors import install_req_from_line
from pipu._internal.resolution.resolvelib.factory import Factory
from pipu._internal.resolution.resolvelib.provider import PipProvider
from pipu._internal.utils.temp_dir import TempDirectory, global_tempdir_manager
from tests.lib import TestData


@pytest.fixture
def finder(data: TestData) -> Iterator[PackageFinder]:
    session = PipSession()
    scope = SearchScope([str(data.packages)], [], False)
    collector = LinkCollector(session, scope)
    prefs = SelectionPreferences(allow_yanked=False)
    finder = PackageFinder.create(collector, prefs)
    yield finder


@pytest.fixture
def preparer(finder: PackageFinder) -> Iterator[RequirementPreparer]:
    session = PipSession()
    rc = InstallCommand("x", "y")
    o = rc.parse_args([])

    with global_tempdir_manager():
        with TempDirectory() as tmp:
            with get_build_tracker() as tracker:
                preparer = RequirementCommand.make_requirement_preparer(
                    tmp,
                    options=o[0],
                    build_tracker=tracker,
                    session=session,
                    finder=finder,
                    use_user_site=False,
                    verbosity=0,
                )

                yield preparer


@pytest.fixture
def factory(finder: PackageFinder, preparer: RequirementPreparer) -> Iterator[Factory]:
    yield Factory(
        finder=finder,
        preparer=preparer,
        make_install_req=install_req_from_line,
        wheel_cache=None,
        use_user_site=False,
        force_reinstall=False,
        ignore_installed=False,
        ignore_requires_python=False,
        py_version_info=None,
    )


@pytest.fixture
def provider(factory: Factory) -> Iterator[PipProvider]:
    yield PipProvider(
        factory=factory,
        constraints={},
        ignore_dependencies=False,
        upgrade_strategy="to-satisfy-only",
        user_requested={},
    )

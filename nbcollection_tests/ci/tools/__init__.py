import os
import pytest
import shutil
import tempfile

from _pytest.fixtures import SubRequest
from nbcollection_tests.ci.tools.integrations import TestRepo
from nbcollection_tests.ci.tools.integrations.datatypes import Template, RepoType


@pytest.fixture
def multi_level_ignore_repo(request: SubRequest):
    ignore_repo = TestRepo(RepoType.Local, Template.MultiLevelIgnore)
    request.addfinalizer(ignore_repo.destroy)
    return ignore_repo.setup().repo_path


@pytest.fixture
def single_collection_repo(request: SubRequest):
    single_collection_repo = TestRepo(RepoType.Local, Template.SingleCollection)
    request.addfinalizer(single_collection_repo.destroy)
    return single_collection_repo.setup().repo_path


@pytest.fixture
def multi_collection_repo(request: SubRequest):
    multi_collection_repo = TestRepo(RepoType.Local, Template.MultiCollection)
    request.addfinalizer(multi_collection_repo.destroy)
    return multi_collection_repo.setup().repo_path


@pytest.fixture
def single_collection_repo__immediate_categories(request: SubRequest) -> str:
    immediate_categories_repo = TestRepo(RepoType.Local, Template.SingleCollectionImmediateCategories)
    request.addfinalizer(immediate_categories_repo.destroy)
    return immediate_categories_repo.setup().repo_path


@pytest.fixture
def single_collection_repo__nth_categories(request: SubRequest) -> str:
    nth_categories_repo = TestRepo(RepoType.Local, Template.SingleCollectionNthCategories)
    request.addfinalizer(nth_categories_repo.destroy)
    return nth_categories_repo.setup().repo_path


@pytest.fixture
def quick_build_collection(request: SubRequest) -> str:
    quick_build_repo = TestRepo(RepoType.Local, Template.QuickBuild)
    request.addfinalizer(quick_build_repo.destroy)
    return quick_build_repo.setup().repo_path


@pytest.fixture
def executed_notebook_collection(request: SubRequest) -> str:
    executed_notebook_repo = TestRepo(RepoType.Local, Template.ExecutedCollection)
    request.addfinalizer(executed_notebook_repo.destroy)
    return executed_notebook_repo.setup().repo_path


@pytest.fixture
def multi_notebook_category(request: SubRequest) -> str:
    multi_notebook_repo = TestRepo(RepoType.Local, Template.MultiNotebookCategory)
    request.addfinalizer(multi_notebook_repo.destroy)
    return multi_notebook_repo.setup().repo_path


@pytest.fixture
def metadata_rich_notebooks(request: SubRequest) -> str:
    metadata_rich_repo = TestRepo(RepoType.Local, Template.MetadataRichNotebooks)
    request.addfinalizer(metadata_rich_repo.destroy)
    return metadata_rich_repo.setup().repo_path


@pytest.fixture
def empty_dir(request: SubRequest) -> str:
    dirpath = tempfile.NamedTemporaryFile().name

    def _remove_empty_dir():
        shutil.rmtree(dirpath)

    os.makedirs(dirpath)
    request.addfinalizer(_remove_empty_dir)
    return dirpath


@pytest.fixture
def immediate_level_repo(request: SubRequest) -> str:
    immediate_level_repo = TestRepo(RepoType.Local, Template.EmptyDirWithGitRemoteUpstream)
    request.addfinalizer(immediate_level_repo.destroy)
    return immediate_level_repo.setup().repo_path


@pytest.fixture
def next_level_repo(request: SubRequest) -> str:
    next_level_repo = TestRepo(RepoType.Local, Template.NextDirWithGitRemoteUpstream)
    request.addfinalizer(next_level_repo.destroy)
    return next_level_repo.setup().repo_path


@pytest.fixture
def git_config_file(request: SubRequest) -> str:
    git_config_repo = TestRepo(RepoType.Local, Template.OnlyGitConfigFile)
    request.addfinalizer(git_config_repo.destroy)
    return git_config_repo.setup().repo_path

@pytest.fixture
def repo_with_html(request: SubRequest) -> str:
    html_repo = TestRepo(RepoType.Local, Template.RepoWithHTML)
    request.addfinalizer(html_repo.destroy)
    return html_repo.setup().repo_path

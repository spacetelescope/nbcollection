import argparse
import git
import logging
import os
import shutil

from nbcollection.ci.commands.datatypes import Site
from nbcollection.ci.constants import SCANNER_ARTIFACT_DEST_DIR

logger = logging.getLogger(__name__)


def run_sync(options: argparse.Namespace) -> None:
    if not os.environ.get('CIRCLE_PULL_REQUEST', None) is None:
        logger.info('Pull Request detected. Skipping Website Publication')
        return None

    if options.site is Site.GithubPages:
        try:
            project_repo = git.Repo(options.project_path)
        except git.exc.InvalidGitRepositoryError:
            raise Exception(f'ProjectPath[{options.project_path}] does not contain a .git folder')

        current_branch = project_repo.head.reference
        try:
            branch = project_repo.heads[options.publish_branch]
        except IndexError:
            branch = project_repo.create_head(options.publish_branch)

        try:
            push_remote = project_repo.remotes[options.publish_remote]
        except IndexError:
            remote_url = os.environ['CIRCLE_REPOSITORY_URL']
            logger.info(f'Using Remote URL: {remote_url}')
            push_remote = project_repo.create_remote(options.publish_remote, remote_url)


        storage_dir = os.path.join(options.project_path, options.artifact_storage_directory)
        from nbcollection.ci.scanner.utils import find_build_jobs
        for build_job in find_build_jobs(options.project_path, options.collection_names, options.category_names, options.notebook_names, True):
            source_path = os.path.join(SCANNER_ARTIFACT_DEST_DIR, build_job.collection.name, build_job.category.name)
            storage_path = os.path.join(storage_dir, build_job.collection.name, build_job.category.name)
            storage_path_dirpath = os.path.dirname(storage_path)
            if not os.path.exists(source_path):
                logger.info(f'Storing Artifact: {build_job.collection.name}.{build_job.category.name}')
                continue

            logger.info(f'Storing Artifact: {build_job.collection.name}.{build_job.category.name}')
            if not os.path.exists(storage_path_dirpath):
                os.makedirs(storage_path_dirpath)

            if os.path.exists(storage_path):
                shutil.rmtree(storage_path)

            shutil.copytree(source_path, storage_path)

        logger.info(f'Pushing Artifacts to Storage Branch: {options.publish_remote} -> {options.publish_branch}')
        project_repo.head.reference = branch
        project_repo.index.add(storage_dir, force=True)
        project_repo.index.commit('Added locally built artifacts')
        push_remote.push(options.publish_branch, force=True)
        project_repo.head.reference = current_branch


    else:
        raise NotImplementedError(options.site)


    # validate_and_parse_inputs(options)
    # command_context = CICommandContext(options.project_path,
    #                                  options.collection_names,
    #                                  options.category_names,
    #                                  options.notebook_names,
    #                                  options.ci_mode)

    merge_context = generate_merge_context(options.project_path, options.org, options.repo_name)
    run_artifact_merge(command_context, merge_context)

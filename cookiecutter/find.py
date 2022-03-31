"""Functions for finding Cookiecutter templates and other components."""
import logging
import os

from cookiecutter.exceptions import NonTemplatedInputDirException

logger = logging.getLogger(__name__)


def find_template(repo_dir, jinja_var_start='{{', jinja_var_end='}}'):
    """Determine which child directory of `repo_dir` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :returns project_template: Relative path to project template.
    """
    logger.debug('Searching %s for the project template.', repo_dir)

    repo_dir_contents = os.listdir(repo_dir)

    project_template = None
    for item in repo_dir_contents:
        if 'cookiecutter' in item and jinja_var_start in item and jinja_var_end in item:
            project_template = item
            break

    if project_template:
        project_template = os.path.join(repo_dir, project_template)
        logger.debug('The project template appears to be %s', project_template)
        return project_template
    else:
        raise NonTemplatedInputDirException

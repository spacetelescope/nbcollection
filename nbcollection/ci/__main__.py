import argparse
import os
import sys

from nbcollection.ci.commands import replicate, build_notebooks, metadata, generate_ci_environment, merge_artifacts, \
        pull_request, site_deployment, sync_notebooks, sync_artifacts

commands = {
  'metadata': metadata,
  'replicate': replicate,
  'build-notebooks': build_notebooks,
  'generate-ci-env': generate_ci_environment,
  'merge-artifacts': merge_artifacts,
  'pull-request': pull_request,
  'site-deployment': site_deployment,
  'sync-notebooks': sync_notebooks,
  'sync-artifacts': sync_artifacts,
}

rendered_commands = '\n    '.join([' '.join(['nbcollection-ci', key]) for key in commands.keys()])
DESCRIPTION = f"""Type `nbcollection-ci <command> -h` for help.

The allowed commands are:

    {rendered_commands}
"""


def main() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            description=DESCRIPTION,
            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("command",
                        help=f"The command you'd like to run. Allowed commands: {list(commands.keys())}")

    args = sys.argv
    options = parser.parse_args(args[1:2])
    if options.command not in commands:
        parser.print_help()
        raise ValueError(f'Unrecognized command: {options.command}\n See the '
                         'help above for usage information')

    # Run the command
    commands[options.command].convert(args)


def run_from_cli():
    sys.path.append(os.getcwd())
    main()


if __name__ == "__main__":
    main()

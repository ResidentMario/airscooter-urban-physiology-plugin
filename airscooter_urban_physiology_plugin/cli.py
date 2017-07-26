import click
# noinspection PyUnresolvedReferences
import urban_physiology_toolkit.workflow_utils as workflow_utils


@click.command()
@click.option('--max-filesize', help='The maximum size (in MB) of resources in the glossary that will be read into the '
                                     'catalog.')
@click.option('--max-columns', help='The maximum size (in number of columns of data) of resources in the glossary that '
                                    'will be read into the catalog.')
def init_catalog(max_filesize, max_columns):
    workflow_utils.init_catalog("glossary.json", ".", max_filesize=max_filesize, max_columns=max_columns)
    workflow_utils.update_dag(root=".")


@click.command()
def finalize_catalog():
    workflow_utils.finalize_catalog(".")
    workflow_utils.update_dag(root=".")

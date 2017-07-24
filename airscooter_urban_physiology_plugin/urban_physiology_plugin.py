import click
# noinspection PyUnresolvedReferences
import urban_physiology_toolkit.workflow_utils as workflow_utils


@click.command()
def init_catalog():
    workflow_utils.init_catalog("glossary.json", ".")
    workflow_utils.update_dag(root=".")


@click.command()
def finalize_catalog():
    raise NotImplementedError("Catalog finalization has not been implemented yet.")

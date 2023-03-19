import click
from .setting import *
from .temp import Structure, CreateFoldersAndFiles

structure = Structure(file_path=os.path.join(templates_dir, "structure.toml"))

@click.group()
def cli():
    pass

@cli.command(name='create', help='Create a python project.')
@click.option('--type', default='basic', help='Which kinds of project structure you want to create.')
@click.option('--name', default='myPythonProject', help='The name for your python project.')
@click.option('--demo', default=False, help='Create a demo python project.')
def create_project(type: str, name: str, demo: bool):
    """
    Parameters
    ----------
    type : str
        Which kinds of project structure you want to create.
    name : str
        The name for your python project.
    demo : bool
        Create a demo python project.
    """
    meta_data.update({"repo_name": name})
    
    if type == 'tiny':
        s = structure.tiny
    
    elif type == 'basic':
        s = structure.basic

    cf = CreateFoldersAndFiles(templates_dir=templates_dir, meta_data=meta_data, **s)
    cf.create()

    if demo:
        create_demo()
    
if __name__ == '__main__':
    cli()
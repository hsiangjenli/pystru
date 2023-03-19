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
    
    meta_data.update({"repo_name": name})
    
    if type == 'tiny':
        s = structure.tiny
    elif type == 'basic':
        s = structure.basic

    cf = CreateFoldersAndFiles(templates_dir=templates_dir, meta_data=meta_data, **s)
    cf.create()

    if demo:
        create_demo()

# @cli.command(name='tiny', help='Build a tiny python project.')
# @click.option('--name', default='myPythonProject', help='The name for your python project.')
# @click.option('--demo', default=False, help='Create a demo python project.')
# def tiny_project(name: str):
#     meta_data.update({"repo_name": name})
#     cf = CreateFoldersAndFiles(templates_dir=templates_dir, meta_data=meta_data, **structure.tiny)
#     cf.create()


# @cli.command(name='basic', help='Build a tiny python project.')
# @click.option('--name', default='myPythonProject', help='The name for your python project.')
# @click.option('--demo', default=False, help='Create a demo python project.')
# def basic_project(name: str):  
#     meta_data.update({"repo_name": name})
#     cf = CreateFoldersAndFiles(templates_dir=templates_dir, meta_data=meta_data, **structure.basic)
#     cf.create()
    

if __name__ == '__main__':
    cli()
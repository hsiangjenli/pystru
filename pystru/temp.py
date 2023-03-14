from jinja2 import Environment, FileSystemLoader
import os, shutil

def set_environment(folder: str, template:str):
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template)
    return template

class CreateFoldersAndFiles:
    def __init__(self, templates_dir, meta_data, **kwargs) -> None:
        self.templates_dir = templates_dir
        self.meta_data = meta_data
        self.kwargs = kwargs
    

    def __create_folders(self):
        for folder in self.kwargs['folders']:
            os.makedirs(name=folder, exist_ok=True)
    

    def __create_files_from_jinja2(self):
        for _, file in self.kwargs['jinja2'].items():
            template = set_environment(folder=self.templates_dir, template=file)
            with open(file, "w", encoding="utf-8") as f:
                f.write(template.render(**self.meta_data))
    
    def __copy_files(self):
        for dst, src in self.kwargs['copy'].items():
            pass
            # shutil.copyfile(dst=dst, src=src)




# def create_folder_file(templates_dir: str, files: list, folders: list, meta_data: dict, **kwargs):
#     for folder in folders:
#         os.makedirs(name=folder, exist_ok=True)
    
#     for file in files:
#         temp = set_environment(folder=templates_dir, template=file)
#         with open(file, "w", encoding="utf-8") as f:
#             f.write(temp.render(**meta_data))
    
#     for dst, src in kwargs.items():
#         shutil.copyfile(dst=dst, src=src)
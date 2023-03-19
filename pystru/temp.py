from jinja2 import Environment, FileSystemLoader
import os, shutil


def set_environment(folder: str, template:str):
    env = Environment(loader=FileSystemLoader(folder))
    template = env.get_template(template)
    return template


class CreateFoldersAndFiles:
    def __init__(self, templates_dir, meta_data, **kwargs) -> None:
        self.templates_dir = templates_dir
        self.files_dir = os.path.join(templates_dir, "files")
        self.meta_data = meta_data
        self.kwargs = kwargs
    

    def create(self):
        self.__create_folders()
        self.__create_files_from_jinja2()
        self.__copy_files()


    def __create_folders(self):
        for folder in self.kwargs['folders']:
            os.makedirs(name=folder, exist_ok=True)
    

    def __create_files_from_jinja2(self):
        for _, file in self.kwargs['jinja2'].items():
            template = set_environment(folder=self.templates_dir, template=file)
            with open(file, "w", encoding="utf-8") as f:
                f.write(template.render(**self.meta_data))
    
    
    def __copy_files(self):
        for _, (dir, file_name) in self.kwargs['files'].items():
            if dir != ".":
                dst = os.path.join(dir, file_name)
            else:
                dst = file_name
            
            shutil.copyfile(dst=dst, src=os.path.join(self.files_dir, dst))



class Structure:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @property
    def structure_data(self):
        import toml
        return toml.load(self.file_path)
    

    @staticmethod
    def inherit_data(parent: dict, child: dict={}):
        child.update(parent)
        return child
    

    @property
    def tiny(self):
        return {
            "jinja2": self.structure_data["tiny"]["jinja2"],
            "files": self.structure_data["tiny"]["files"],
            "folders": self.structure_data["tiny"]["folders"],
        }


    @property
    def basic(self):
        basic_jinj2 = self.inherit_data(
            parent=self.structure_data["tiny"]["jinja2"], 
            child=self.structure_data["basic"]["jinja2"]
        )
        basic_files = self.inherit_data(
            parent=self.structure_data["tiny"]["files"], 
            child=self.structure_data["basic"]["files"]
        )
        basic_folders = self.inherit_data(
            parent=self.structure_data["tiny"]["folders"], 
            # child=self.structure_data["basic"]["folders"]
        )

        return {
            "jinja2": basic_jinj2,
            "files": basic_files,
            "folders": basic_folders,
        }

# def create_folder_file(templates_dir: str, files: list, folders: list, meta_data: dict, **kwargs):
#     for folder in folders:
#         os.makedirs(name=folder, exist_ok=True)
    
#     for file in files:
#         temp = set_environment(folder=templates_dir, template=file)
#         with open(file, "w", encoding="utf-8") as f:
#             f.write(temp.render(**meta_data))
    
#     for dst, src in kwargs.items():
#         shutil.copyfile(dst=dst, src=src)
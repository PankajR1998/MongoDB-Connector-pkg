from setuptools import find_packages,setup
from typing import List
from pathlib import Path
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "MongoDB-Connector-pkg"
PKG_NAME = "mongohelper" # by this name package will be visible.
AUTHOR_USER_NAME = "PankajR1998"
AUTHOR_EMAIL = "rawatpankaj9919@gmail.com"



setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/makedown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    # install_requires=get_requirements(Path('./requirements.txt'))
)   

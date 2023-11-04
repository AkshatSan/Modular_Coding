from setuptools import find_packages, setup
from typing import List

hyphon="-e ."


def get_requiremenets(filepath:str) -> List[str]: 
    requirements=[]
    with open(filepath) as file_obj:
        requirements= file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hyphon in requirements:
            requirements.remove(hyphon)

setup(name='ML_Project',
      version='1.0',
      description='ML pipeline project',
      author='Akshat Pandey',
      author_email='aaaakshaat@gmail.com',
      packages=find_packages(),
      install_requires=get_requiremenets("requirements.txt")
     )


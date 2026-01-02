from typing import List
from setuptools import setup,find_packages


def get_requirements()-> List[str]:

    requirements_list : List[str] = []

    try : 
        with open('requirements.txt','r') as file : 
            lines = file.readlines()
            for line in lines : 
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt is not found") 
        
    return requirements_list

print(get_requirements())

setup(
    name = "name",
    version = "0.0.1",
    author = "Gaber",
    packages = find_packages(),
    install_requires=get_requirements()
)
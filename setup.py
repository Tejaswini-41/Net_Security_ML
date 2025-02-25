'''

use for packaging and distributing python projects.

used by setup tools to define the config of project such as metadata, dependencies, etc.


'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
     function will return list of req
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())

setup(
    name="networkSecurity",
    version="0.0.1",
    author="Tejaswini",
    author_email="tejaswinidurge41@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


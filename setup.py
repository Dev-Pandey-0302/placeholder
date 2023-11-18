from setuptools import setup, find_packages
from typing import List

Ending='-e .'

def get_requirements(filename:str)->List[str]:
    '''
    this function will read the requirements.txt file and return the list of requirements
    '''
    requirements = []
    with open(filename) as fh:
        for line in fh:
            if(line!=Ending):
                requirements.append(line.strip())
    return requirements

setup(
    name='mlproject-temp',
    version='0.0.1',
    author='Dev',
    author_email='dev.pandey.0302@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
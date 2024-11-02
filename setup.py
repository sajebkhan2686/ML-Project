from setuptools import find_packages,setup #finds automatically all the packages in ml directory which are created
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #will replace blank line

        #do not want "-e ." because it will automatically trigger
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# Metadata and installation configuration
setup(
    name='mlproject',
    version='0.0.1',
    author='Sajeb Khan',
    author_email='shazebk2686@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')

)
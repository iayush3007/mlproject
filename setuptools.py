from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the provided file.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            # Remove newline characters and empty lines
            requirements = [req.strip() for req in requirements if req.strip()]
            # Remove '-e .' if present
            requirements = [req for req in requirements if req != HYPEN_E_DOT]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return requirements
        
setup(
    name='mlproject', 
    version='0.0.1',
    author='Ayush',
    author_email='12212030@nitkkr.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

from setuptools import setup ,find_packages
from typing import List

def get_requirements()-> List[str]:
    
    requirement_list:List[str] = []
    return requirement_list
    
setup(
    name = "sensor",
    version = "0.1",
    author="JatinKumarMahaldar",
    author_email="jatinkumarmahaldar@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements() #["pymongo==4.2.0"],
)



from setuptools import setup, find_packages
import os

bobo_packages = [f"Bobo.{package}" for package in find_packages(where=os.path.join(os.path.dirname(__file__), 'src'))]
bobo_packages.append("bobo")

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = [line.strip() for line in f.read().splitlines()]

setup(
    name='Bobo',
    version="0.1",
    packages=traduc_packages,
    include_package_data=True,
    package_dir={"Bobo": "src"},
    url='https://github.com/javibg96/traductor_csv/',
    author='Javier Blasco',
    install_requires=requirements,
    author_email="blascogarcia.javier@outlook.com",
    description='asistente personal desarrollado en python'
)


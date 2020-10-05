import setuptools
from sys import platform


with open('README.md', 'r') as readme_fp:
    long_description = readme_fp.read()

with open('requirements.txt', 'r') as req_fp:
    required_libs = req_fp.readlines()


setuptools.setup(
    name='ciphit',
    scripts=['ciphit/ciphitapp.py'],
    description='ciphit is a cryptography CLI-tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2.0',
    author='Sagar Kumar',
    license='MIT',
    packages=setuptools.find_packages(exclude=['install.sh']),
    install_requires=required_libs,
    url='https://github.com/sgrkmr/ciphit',
    keywords='cli commandline user-interface ui cryptography',
    python_requires='>=3.7',
    entry_points={
    'console_scripts': [
        'ciphit = ciphit.ciphitapp:main',
        ],
    },
)
from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author="David Marsh",
    author_email="dfmarsh95@gmail.com",
    description="Snapshotalyzer is a tool that manages AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/davidfmarsh/snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
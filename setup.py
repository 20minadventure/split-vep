from setuptools import setup, find_packages


setup(
    name="helloworld",
    version="2016.12.24",
    description="",
    long_description='README.md',
    author="JH",
    author_email="email@gmail.com",
    url="",
    packages=find_packages(),
    license='LICENSE',
    entry_points={
        'console_scripts': [
            'aloha = analysis.helloworld:hello'
        ]
    },
)

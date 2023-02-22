from setuptools import setup


setup(
    name="helloworld",
    version="2016.12.24",
    description="",
    long_description='README.md',
    author="JH",
    author_email="email@gmail.com",
    url="",
    py_modules=['helloworld'],
    license='LICENSE',
    entry_points={
        'console_scripts': [
            'aloha = analysis.helloworld:hello'
        ]
    },
)

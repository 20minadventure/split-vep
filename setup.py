from setuptools import setup, find_packages


setup(
    name="helloworld",
    version="2023.0.1",
#    description="",
#    long_description='README.md',
#    author="JH",
#    author_email="email@gmail.com",
#    url="",
    packages=find_packages(),
#    license='LICENSE',
    package_data={'helloworld': ['utils/file']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'aloha = analysis.helloworld:hello'
        ]
    },
)

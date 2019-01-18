from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='pydecorator',
    version='1.0',
    author='Lucian Cooper',
    url='https://github.com/luciancooper/pydecorator',
    description='Python Decorator Functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='decorator utility',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=['pydecorator'],
    install_requires=['numpy','pandas'],
)

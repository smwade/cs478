from distutils.core import setup

setup(
    name='MLTools',
    version='0.7',
    author='Sean Wade',
    author_email='seanwademail@gmail.com',
    packages=['mltools', 'mltools.models'],
    license='Apache-2.0',
    description='Machine Learning tools and models',
    long_description=open('README.md').read(),
)

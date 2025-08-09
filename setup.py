from setuptools import setup, find_packages

setup(
    name='log-candy',
    version='0.1.4',
    description='A simple Python logging utility for colorful terminal output',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sabino Roccotelli',
    author_email='sabinoroccotelli@icloud.com',
    url='https://github.com/SabeeenoGH/log-candy',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
from setuptools import setup


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='holidays',
    version='0.1.0',
    author='Marco Ramos',
    author_email='marco.ramos@galp.com',
    description='Calculate holidays dates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='_',
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Utilities',
        'Typing :: Typed'
    ],
    keywords=['python', 'holidays', 'Portugal', 'Spain'],
    packages=['holidays'],
    include_package_data=True,
    package_data={
        '':['holidays.json']
    },
    install_requires=[
        'python-dateutil>=2.8.1',
        'pandas>=1.2.2',
    ],
    python_requires='>=3.8'
)
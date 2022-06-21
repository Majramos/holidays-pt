from setuptools import setup


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setup(
        name='holidays',
        version='0.1.0',
        author='Marco Ramos',
        author_email='majramos@gmail.com',
        description='Calculate holidays dates for Portugal',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://gitlab.com/majramos/holidays-pt',
        classifiers=[
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Topic :: Utilities',
            'Typing :: Typed'
        ],
        keywords=['python', 'holidays', 'Portugal'],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        include_package_data=True,
        python_requires='>=3.9'
        package_data={
            '':['holidays.json']
        },
        install_requires=[
            'python-dateutil>=2.8.1',
            'pandas>=1.2.2',
        ],
        extras_require={
            'dev': [
                'jupyterlab==3.2.9',
                'jupyterlab-execute-time==2.1.0',
                'jupyterlab-theme-solarized-dark @ git+https://github.com/Majramos/jupyterlab-theme-solarized-dark',
            ],
        }
        
    )
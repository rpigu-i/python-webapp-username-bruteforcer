from setuptools import setup, find_packages


setup(
    name='username-bruteforcer',
    version='0.0.1',
    description='Username bruteforcer for web applications written in Python',
    maintainer='@patamechanix',
    license='MIT',
    url='https://github.com/patamechanix/python-webapp-username-bruteforcer',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'username-bruteforcer = username_bruteforcer.__main__:main'
        ]
    }
)

from setuptools import setup, find_packages


setup(
    name='username-bruteforcer',
    version='2.0.0',
    description='Username bruteforcer for web applications written in Python',
    maintainer='@rpigu-i',
    license='MIT',
    url='https://github.com/rpigu-i/python-webapp-username-bruteforcer',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'username-bruteforcer = username_bruteforcer.__main__:main'
        ]
    },
    install_requires=[
      'requests'
    ]
)

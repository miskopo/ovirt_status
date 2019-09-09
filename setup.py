from setuptools import setup
setup(
    name='ovirt_status',
    version='0.0.1',
    packages=['ovirt_status'],
    entry_points={
        'console_scripts': [
            'ovirt_status = ovirt_status.__main__:main'
         ]
    })

from setuptools import setup

setup(
    name='Trainement SS',
    version='1.0',
    py_modules=['trainementss'],
    include_package_data=False,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        trainementss=trainementss:cli
    ''',
)

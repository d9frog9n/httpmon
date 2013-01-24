from setuptools import setup

setup(name='httpmon',
    version='0.0.1',
    description='HttpMon',
    author='Dmi Baranov',
    author_email='dmi.baranov@gmail.com',
    url='http://github.com/d9frog9n/httpmon',
    packages=['httpmon'],
    package_data={'twisted.plugins': ['twisted/plugins/httpmon.py']},
    zip_safe=False
)
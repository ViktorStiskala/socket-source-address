from setuptools import setup, find_packages


setup(
    name='socket-source-address',
    version='0.1',
    author='Viktor Stískala',
    author_email='viktor@stiskala.cz',
    description='Monkey patch for socket.create_connection with explicit source address',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
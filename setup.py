from setuptools import setup

setup(
    name='dcc-receive',
    version='0.1',
    packages=['dcc-receive'],
    install_requires=[
        'pyserial',
        'enum',
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
    ],
    url='https://github.com/riverdale-soc/nanorecieve',

    description="UART port listener to receive incoming MOB (Man-Overboard) Packets from ESP32 Submersion Handler.",
    author_email='Dlyalikov01@manhattan.edu',
    author='Dmitri Lyalikov'
)
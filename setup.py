from setuptools import setup

setup(
    name='nmap_vscan_fix',
    version='1.1.5',
    author='An0m',
    author_email='',
    license='MIT',
    long_description_content_type="text/x-rst",
    description='nmap service and application version detection (without nmap installation)',
    long_description=open('README.rst').read(),
    keywords='nmap vscan fingerprint recognition security',
    packages=['nmap_vscan'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


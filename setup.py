# coding=utf8

from setuptools import setup

version = '0.2.5'

setup(
    name="buffer-api",
    version=version,
    author="barisariburnu",
    author_email="barisariburnu@gmail.com",
    description="Buffer API library client for python",
    license="GNU GENERAL PUBLIC LICENSE",
    keywords="Buffer API library client for python",
    url='https://github.com/barisariburnu/buffer-api',
    download_url='https://github.com/barisariburnu/buffer-api/releases/tag/' + version,
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'buffer',
        'buffer.api',
        'buffer.error',
        'buffer.http_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

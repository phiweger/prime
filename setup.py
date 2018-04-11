from setuptools import setup

setup(
    name="prime",
    version='v0.1',
    install_requires=[
        'click',
        'biopython',
        'numpy',
        'primer3-py',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    entry_points={'console_scripts': ['prime = prime.__main__:cli']}
    )


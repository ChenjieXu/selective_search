from setuptools import setup, find_packages

setup(
    name="selective_search",
    version="0.0.1",
    url="https://github.com/ChenjieXu/selective_search",
    description="Selective Search in Python",
    author="Chenjie Xu",
    keywords='rcnn',
    packages=find_packages(),
    license='MIT',
    classifiers=[  
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requirements,
)

from setuptools import setup, find_packages

with open('README.md', encoding="utf8") as f:
    readme = f.read()

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name="selective_search",
    version="0.1.0",
    url="https://github.com/ChenjieXu/selective_search",
    description="Selective Search in Python",
    long_description=readme,
    author="Chenjie Xu",
    author_email="cxuscience@gmail.com",
    keywords='rcnn',
    packages=find_packages(),
    license='MIT',
    classifiers=[  
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=reqs.strip().split('\n'),
)

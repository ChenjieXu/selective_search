from setuptools import setup, find_packages

with open('README.md', encoding="utf8") as f:
    readme = f.read()

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name="selective_search",
    version="0.1.2",
    url="https://github.com/ChenjieXu/selective_search",
    description="Selective Search in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Chenjie Xu",
    author_email="cxuscience@gmail.com",
    keywords='rcnn',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
    ],
    install_requires=reqs.strip().split('\n'),
)

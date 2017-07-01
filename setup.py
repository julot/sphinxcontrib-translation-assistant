from setuptools import setup, find_packages


description = (
    'Sphinx extension to view Translation Assistant file'
)

with open('README.rst', 'r', encoding='utf8') as f:
    long_description = f.read()

requires = [
    'Sphinx>=0.6',
]

keywords = [
    'sphinx',
    'sphinxcontrib',
    'translation assistant',
]

setup(
    name='sphinxcontrib-translation-assistant',
    version='0.2.0',
    url='https://github.com/julot/sphinxcontrib-translation-assistant',
    license='MIT',
    author='Andy Yulius',
    author_email='julot@gmail.com',
    description=description,
    long_description=long_description,
    keywords=' '.join(keywords),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    test_suite="tests",
)

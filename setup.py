import json
import setuptools

with open('config.json', 'r') as fh:
    version = json.load(fh)['version']

with open('requirements.txt', 'r') as fh:
    install_requires = fh.readlines()

setuptools.setup(
    name='dottybot',
    version=version,
    description='Discord bot that converts emotes to braille unicode',
    author='mieux2',
    url='https://github.com/mieux2/dottybot',
    packages=['dottybot'],
    python_requires='>=3.7',
    license='MIT',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent'
    ],
    include_package_data=True
)

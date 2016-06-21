from setuptools import setup

setup(name='bigpy',
    version='0.1',
    description='Make things easier for data analyis and automation',
    author='Lee Seongjoo',
    author_email='seongjoo@codebasic.co',
    py_modules=['mail'],
    packages=['webscrap', 'office'],
    install_requires=[
        'imapclient',
        'python-docx'
    ])

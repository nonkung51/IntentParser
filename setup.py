from setuptools import setup
from setuptools import find_packages


setup(name='Simple-Intent-Parser',
      version='1.5.9',
      description='Use to parse an intent easily.',
      author='Nonthakon Jitchiranant',
      author_email='non_thakon@hotmail.com',
      url='https://github.com/nonkung51/IntentParser',
      download_url='https://github.com/nonkung51/IntentParser/archive/master.zip',
      license='Apache-2.0',
      install_requires=['nltk', 'gensim'],
      packages=find_packages())

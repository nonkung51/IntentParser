from setuptools import setup
from setuptools import find_packages


setup(name='intentparser',
      version='1.5.14',
      description='Use to parse an intent easily.',
      author='Nonthakon Jitchiranant',
      author_email='non_thakon@hotmail.com',
      url='https://github.com/nonkung51/IntentParser',
      download_url='https://github.com/nonkung51/IntentParser/archive/master.zip',
      license='Apache-2.0',
      install_requires=['gensim'],
      packages=find_packages())

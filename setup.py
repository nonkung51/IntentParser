from setuptools import setup
from setuptools import find_packages


setup(name='Simple-Intent-Parser',
      version='1.5.9',
      classifiers=[
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: Apache-2.0',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5'
        ],
      description='Use to parse an intent easily.',
      author='Nonthakon Jitchiranant',
      author_email='non_thakon@hotmail.com',
      url='https://github.com/nonkung51/IntentParser',
      download_url='https://github.com/nonkung51/IntentParser/archive/master.zip',
      license='Apache-2.0',
      install_requires=['nltk', 'gensim'],
      keywords='ai chatbot intentparser',
      packages=find_packages(exclude=['examples']),)

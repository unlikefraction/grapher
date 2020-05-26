from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'grapher',
  # other arguments omitted
  long_description=long_description,
  long_description_content_type='text/markdown'
  packages = ['grapher'],
  version = 'v1.3',
  license='MIT',
  description = 'Compare any number of Mathematical Equations and their graphs to see the level of similarity betweeb them in just one line of code. Eg: Taylor Polynomial',
  author = 'Shubham Gupta',
  author_email = 'thecodinghumans@gmail.com',
  url = 'https://github.com/ShubhamGupta-tch/grapher',
  download_url = 'https://github.com/ShubhamGupta-tch/grapher/archive/v1.3.tar.gz',
  keywords = ['maths', 'equations', 'graphs', 'Compare graphs', 'plot graphs', 'mathematics', 'graph comparision', 'comparing equations', 'equations comparision'],
  install_requires=[
          'matplotlib',
          'numpy',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',
    'Framework :: Matplotlib',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Physics',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)

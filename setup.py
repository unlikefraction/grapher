from distutils.core import setup

setup(
  name = 'grapher',
  packages = ['grapher'],
  version = 'v1.7',
  license='MIT',
  description = 'Compare any number of Mathematical Equations and their graphs to see the level of similarity betweeb them in just one line of code. Eg: Taylor Polynomial',
  long_description='''
    This is a Mathematical Grpah Plotting Library that can be used to compare graphs of different equations.\n
    Now, you can even see the graph of the differentation of any function just by using  `d("func")`\n
    Complete Documentation: https://github.com/ShubhamGupta-tch/grapher \n
  ''',
  author = 'Shubham Gupta',
  author_email = 'thecodinghumans@gmail.com',
  url = 'https://github.com/ShubhamGupta-tch/grapher',
  download_url = 'https://github.com/ShubhamGupta-tch/grapher/archive/v1.7.tar.gz',
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

from setuptools import find_packages, setup

"""with this install works only if numpy is already installed, otherwise fails on wheel."""

setup(
  name='pyXsurf',
  version='0.1.25',
  description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
  packages=find_packages(),
  url='https://github.com/vincenzooo/pyXSurf',
  author='Vincenzo Cotroneo',
  author_email='vincenzo.cotroneo@inaf.it',
  install_requires=['numpy'],
  package_dir={'dataIO': 'pyxsurf/dataIO'}
)

from setuptools import find_packages

# or
from setuptools import find_namespace_packages

'''
#from https://docs.pytho
n.org/3/distutils/setupscript.html

from distutils.core import setup

setup(    name='pyXsurf',
    version='0.1.1',
    packages=['pyXsurf'],
    description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
    url='https://github.com/vincenzooo/pyXSurf',
    author='Vincenzo Cotroneo',
    author_email='vincenzo.cotroneo@inaf.it',
    #url='https://github.com/vincenzooo/pyXSurf',
    )
'''     
     
'''

from setuptools import setup
setup(
    name='pyXsurf',
    version='0.1.1',
    packages=['pyXsurf'],
    description="Python library for X-Ray Optics, Metrology Data Analysis and Telescopes Design.",
    url='https://github.com/vincenzooo/pyXSurf',
    author='Vincenzo Cotroneo',
    author_email='vincenzo.cotroneo@inaf.it',
    keywords=['surfaces', 'metrology', 'PSD'],
    tests_require=[
        'pytest'
    ],
    package_data={
        # include json and pkl files
        '': ['*.json', 'models/*.pkl', 'models/*.json'],
    },
    include_package_data=False,
    python_requires='>=3'
)

# from 

'''
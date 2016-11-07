from distutils.core import setup
from pip.req import parse_requirements

setup(name='test-aviary',
      version='1.0',
      description='Test Aviary',
      install_requires=get_requirements('requirements.txt')
      )

def get_requirements(filename):
    reqs = parse_requirements(filename, session=None)

    return [str(r.req) for r in reqs]


from setuptools import setup

version = "1.0.0"

requirements = [
    "Flask==3.1.2",
    "Flask-Bootstrap==3.3.7.1",
]

setup(name='paint-calculator',
      version=version,
      description='App to create web tests against',
      author='Joe Carlyon',
      author_email='JoeCarlyon@gmail.com',
      url='https://github.com/joecarlyon/paint-calculator',
      install_requires=requirements,
      packages=['paint_calculator'],
      )

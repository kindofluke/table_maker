from setuptools import setup

setup(name='table maker',
      version='0.1',
      description='Small Command Line script to get the column names from csv files',
      url='http://github.com/storborg/funniest',
      author='luke',
      author_email='lukeshulman.com',
      license='MIT',
      packages=['table_maker'],
      zip_safe=False,
      entry_points={
          'console_scripts':['tablem=table_maker.table_maker:print_and_copy']
      })
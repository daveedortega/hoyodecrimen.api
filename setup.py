from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='Hoyo de Crimen',
      author='Diego Valle-Jones',
      author_email='diegovalle@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.10.1', 'MarkupSafe' , 'Flask-SQLAlchemy==1.0', 
                        'SQLAlchemy==0.9.3', 'redis==2.9.1','Flask-Cache==0.12',
                        'GeoAlchemy2'==0.2.4],
     )

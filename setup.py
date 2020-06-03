from distutils.core import setup


setup(
    name='nhttp',
    version='1.2build',
    description='A portable http server package',
    author='LaomoBK',
    packages=['nhttp', 'nhttp.server', 'nhttp.constant',
              'nhttp._internal']
)

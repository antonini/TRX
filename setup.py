try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TRX',
    'author': 'Kyle Maxwell, based on Paterva\'s library',
    'url': 'https://github.com/krmaxwell/TRX',
    'download_url': 'https://github.com/krmaxwell/TRX',
    'author_email': 'krmaxwell@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TRX'],
    'scripts': [],
    'name': 'TRX'
}

setup(**config)

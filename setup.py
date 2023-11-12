from setuptools import setup

setup(
    name='anomalydetector-evt',
    version='0.0.1',
    description='Paquete para detección de anomalías mediante Extrem Value Theory',
    url='https://github.com/angmnz/anomalydetector-evt',
    author='Angie Mendez',
    author_email='angiedmc98@gmail.com',
    license='unlicense',
    packages=['anomalydetector_evt'],
    intall_requires=['numpy', 'scipy', 'pandas'],
    zip_safe=False
)


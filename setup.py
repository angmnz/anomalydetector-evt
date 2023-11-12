from setuptools import setup, find_packages

setup(
    name='anomalydetector-evt',
    version='0.0.1',
    description='Paquete para detección de anomalías mediante Extrem Value Theory',
    url='https://github.com/angmnz/anomalydetector-evt',
    author='Angie Mendez',
    author_email='angiedmc98@gmail.com',
    license='unlicense',
    packages=find_packages(),
    intall_requires=['numpy', 'scipy', 'pandas'],
    zip_safe=False
)


from setuptools import setup, find_packages

setup(
    name='SendEmailAutomatic',
    version='1.0',
    description='Send mail Proveedores',
    author='Wilmer Serrano | @IIpapuII',
    author_email= 'wilmer3428@gmail.com',
    url='https://github.com/IIpapuII/SendEmailAutomatic.git',
    packages=find_packages(),
    install_requirements =[
        'numpy==1.24.2',
        'pandas==1.5.3',
        'python-dateutil==2.8.2'
        'python-dotenv==1.0.0'
        'pytz==2022.7.1'
        'six==1.16.0'
    ]
)
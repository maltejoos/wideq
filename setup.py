from setuptools import setup


setup(
    name='wideq',
    version='0.0.0',
    description='LG SmartThinQ API client',
    author='wkd8176',
    author_email='wkd8176@gmail.com',
    url='https://github.com/wkd8176/wideq',
    license='MIT',
    platforms='ALL',
    install_requires=['requests'],
    py_modules=['wideq'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

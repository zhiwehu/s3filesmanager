from setuptools import setup, find_packages


setup(
    name='s3filesmanager',
    version='0.4.2',
    description='AWS S3 files manager',
    long_description=open('docs/index.rst').read(),
    author='Jeffrey Hu',
    author_email='zhiwehu@gmail.com',
    url='https://github.com/zhiwehu/s3filesmanager',
    install_requires=['django >= 1.5',
                      'South >= 0.7.6',
                      'django-model-utils >= 1.1.0',
                      'django-bootstrap-toolkit',
                      'PIL == 1.1.7',
                      'sorl-thumbnail >= 11.12',
                      'boto >= 2.9.0',
                      'django-storages >= 1.1.8',
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

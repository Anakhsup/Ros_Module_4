from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'back_in_time'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akshup',
    maintainer_email='akshup@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'back_in_time_broadcaster = back_in_time.back_in_time_broadcaster:main',
            'back_in_time_listener = back_in_time.back_in_time_listener:main',
        ],
    },
)

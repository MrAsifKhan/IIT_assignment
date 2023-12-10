from setuptools import find_packages, setup

package_name = 'image_processing_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/image_processing.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asif',
    maintainer_email='pattanasifkhan97@gmail.com',
    description='IIT project ROS task',
    license='AK',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node1 = image_processing_pkg.node1:main',
            'node2 = image_processing_pkg.node2:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'robotarm_control_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aa',
    maintainer_email='rlawjd923@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robotarm_controller_node = robotarm_control_package.robotarm_controller_node:main',
            'task_manager = robotarm_control_package.task_manager:main'
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'hw_int_py_pkg'

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
    maintainer='fk',
    maintainer_email='fk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "SerialCom = hw_int_py_pkg.serial_com_node:main",
            "RCStatePub = hw_int_py_pkg.rcstate_pub_node:main" 
        ],
    },
)

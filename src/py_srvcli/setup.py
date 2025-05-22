from setuptools import find_packages, setup

package_name = 'py_srvcli'

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
    maintainer='prometheus',
    maintainer_email='gabe.susman@gmail.com',
    description='The Argus Robotic Client enables the operator to perform QA, testing, and administration of the Argus Robotic Simulation system.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = py_srvcli.client_member_function:main',
        ],
    },
)

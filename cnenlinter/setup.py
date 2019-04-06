from setuptools import setup

setup(
    name='cnenlinter',
    version='0.1',
    description='Use Regex rules to fix common lint problems in Chinese-English docs',
    author='xiaolai',
    author_email='lixiaolai@gmail.com',
    license='MIT',
    py_modules=['cnenlinter'],
    install_requires=[
        'Click',
        'PyYAML',
    ],
    entry_points='''
        [console_scripts]
        cnenlinter=cnenlinter:cnenlinter
    ''',
    include_package_data=True,
)
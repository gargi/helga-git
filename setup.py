from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="helga-git",
    version=version,
    description=('Helga plugin to check if any of my PRs have enough LGTM'),
    author='Gargi R',
    author_email='grajadhyaksha@pindrop.com',
    packages=find_packages(),
    py_modules=['helga_git'],
    include_package_data=True,
    zip_safe=True,
    entry_points=dict(
        helga_plugins=[
            'checkLGTM = helga_git:checkLGTM'
        ],
    ),
)

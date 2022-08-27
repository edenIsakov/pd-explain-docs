from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pd_explain',
    version='0.0.1',
    description="Create explanation to dataframe",
    long_description=long_description,  # Long description read from the readme file
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    project_urls={
        'Git': 'https://github.com/edenIsakov/pd-expain',
    },
    install_requires=[
        'wheel',
        'pandas',
        'numpy',
        'python-dotenv',
        'singleton-decorator',
        'explain_ed@git+ssh://git@github.com/TAU-DB/ExplainED.git@create-python-package#egg=explain_ed',
        'subtab@git+ssh://git@github.com/KathyRaz/SubTab.git@create_as_package#egg=subtab'
    ]

)

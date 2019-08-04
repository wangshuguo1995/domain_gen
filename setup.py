from setuptools import setup


setup(
    name="domain_gen",
    version="0.0.1",
    packages=["domain_gen"],
    package_data={
        'domain_gen': [
                'resources/*',
            ]
    },
    include_package_data=True,
    url="https://github.com/rootVIII/domain_gen",
    license="MIT",
    author="rootVIII",
    description="Search for random, available, 2-word domain names",
    entry_points={
        "console_scripts": [
            "domain_gen=domain_gen.domain_gen:main"
        ]
    },
    data_files=[
        ('words', ['resources/word_list.json']),
        ('config', ['resources/config.yml'])
    ]
)

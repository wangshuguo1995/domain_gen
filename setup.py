from setuptools import setup


setup(
    name="domain_gen",
    version="0.0.1",
    packages=["domain_gen"],
    package_data={
        'domain_gen': [
                'domain_gen/domain_gen/resources/*',
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
        ('words', ['domain_gen/gomain_gen/word_list.json']),
        ('config', ['domain_gen/gomain_gen/config.yml'])
    ]
)

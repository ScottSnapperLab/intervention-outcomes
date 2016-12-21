"""Install setup."""
import setuptools

setuptools.setup(
    name="intervention_outcomes",
    version="0.0.1",
    url="git@github.com:ScottSnapperLab/intervention-outcomes.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="Attempting to predict success of outcomes to VEOIBD interventions.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},


    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
    "console_scripts": [
        "intervention-outcomes = intervention_outcomes.cli.main:run",
        ]
    },
)

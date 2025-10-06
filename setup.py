import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ubg_gprpy_fork",
    version="0.0.1",
    author="Fork: Maximilian Weigand, Original GPRPy: Alain Plattner",
    author_email="mweigand@geo.uni-bonn.de",
    description="".join((
        "GPRPy - open source ground penetrating radar processing ",
        "and visualization",
        "Based on GPRPy (https://github.com/NSGeophysics/GPRPy)"
    )),
    entry_points={'console_scripts': ['gprpy = gprpy.__main__:main']},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/geophysics-ubonn/ubg_GPRPy_fork/",
    packages=['gprpy'],
    package_data={
        'gprpy': [
            'exampledata/GSSI/*.DZT',
            'exampledata/GSSI/*.txt',
            'exampledata/SnS/ComOffs/*.xyz',
            'exampledata/SnS/ComOffs/*.DT1',
            'exampledata/SnS/ComOffs/*.HD',
            'exampledata/SnS/WARR/*.DT1',
            'exampledata/SnS/WARR/*.HD',
            'exampledata/pickedSurfaceData/*.txt',
            'examplescripts/*.py',
            'toolbox/splashdat/*.png',
            'toolbox/*.py',
            'irlib/*.py',
            'irlib/external/*.py'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'tqdm',
        'numpy',
        'scipy',
        'matplotlib',
        'Pmw',
        'pyevtk'
    ]
)

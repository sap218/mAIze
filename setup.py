import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='maize',
      version='1.0.0.0',
      description='Command Line Chatter',
      url='https://github.com/sap218/mAIze',
      author='Samantha C Pendleton',
      author_email='samanfapendle@outlook.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
      zip_safe=False,
      entry_points = {'console_scripts': ['maize=maize.maize:main']},
      include_package_data = True
)

from setuptools import setup, find_packages

setup(
    name="muda_imagem_9_16",
    version="0.1.0",   
    author="Fábio Almeida",
    author_email="fabiobdalmeida@gmail.com",
    description="A tool to resize images to 9:16 format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fabiobdalmeida/muda_imagem_9_16",
    packages=find_packages(),  # Automatically finds packages in the folder
    install_requires=[
        "pillow"  # List dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "muda-imagem=muda_imagem_9_16.main:main",  # Creates a CLI command
        ],
    },
)

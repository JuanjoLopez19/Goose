from setuptools import setup, find_packages

setup(
    name="goose_prank_downloader",
    version="0.1.0",
    description="A short description of your project",
    author="Juanjolopez19",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["wheel", "winshell", "pywin32"],
)

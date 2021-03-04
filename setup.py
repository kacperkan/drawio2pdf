import sys
from pathlib import Path

from setuptools import setup

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="drawio2pdf",
    description="Scrpit to convert your beautiful draw.io drawings into pdfs.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="automation graphics inkscape drawio pdf",
    author="Kacper Kania",
    author_email="kacp.kania@gmail.com",
    url="https://github.com/kacperkan/drawio2pdf",
    license="MIT",
    packages=["drawio2pdf"],
    package_dir={"": "."},
    python_requires=">=3.6.2",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["drawio2pdf=drawio2pdf:main"]},
)

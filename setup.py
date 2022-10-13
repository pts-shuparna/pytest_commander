"""Setup script for PyTest web UI."""
import setuptools


def main():
    with open("README.md") as f:
        long_description = f.read()

    setuptools.setup(
        name="pytest_commander",
        version="0.0.2",
        author="Shuparna Deb",
        author_email="shuparna@pass-testing.de",
        description="An interactive GUI test runner for PyTest",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pts-shuparna/pytest_commander",
        packages=setuptools.find_packages(include=['pytest_commander']),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
        install_requires=[
            "pytest>=6.2.4, <7.0.0",
            "marshmallow>=3.11.1, <4.0.0",
            "marshmallow-enum>=1.5.1, <2.0.0",
            "flask>=1.1.2, <2.0.0",
            "flask_socketio>=5.0.1, <6.0.0",
            "eventlet>=0.31.0, <1.0.0",
            "watchdog>=2.1.0, <3.0.0",
        ],
        dependency_links=[
            'https://github.com/pts-shuparna/pytest_commander.git@webui_for_pytest#egg=pytest_commander'
        ],
        include_package_data=True,
        entry_points={
            "console_scripts": ["pytest_commander = pytest_commander.__main__:main"]
        },
    )


if __name__ == "__main__":
    main()

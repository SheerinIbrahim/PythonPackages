from setuptools import setup, find_packages

setup(
    name="handtrackingmodule",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "mediapipe"
    ],
    author="Sheerin",
    author_email="sheerinsultana96@gmail.com",
    description="Simple Hand Tracking Module using OpenCV and MediaPipe",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SheerinSultana/PythonPackages/tree/de9b8ba97dcccdcbcce2244b18f48f963738a173/handtrackingmodule",  # if you have github
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)

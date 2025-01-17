import os
import sys

def create_project_structure(project_name, version):
    os.mkdir(project_name)
    os.chdir(project_name)
    with open('__init__.py', 'w') as f:
        f.write('from .whlcode import hello_world')
    with open('whlcode.py', 'w') as f:
        f.write("def hello_world():\n    print('Hello,world!')")
    os.chdir('..')
    with open('LICENSE', 'w') as f:
        f.write("MIT License\n\nCopyright (c) [year] [fullname]\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the 'Software'), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.")
    with open('README.md', 'w') as f:
        f.write(f"# {project_name}")
    with open('setup.py', 'w') as f:
        f.write(f"from setuptools import setup, find_packages\n\nsetup(\n    name='{project_name}',\n    version='{version}',\n    packages=find_packages(),\n)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_project.py <project_name> <version>")
        sys.exit(1)
    project_name = sys.argv[1]
    version = sys.argv[2]
    create_project_structure(project_name, version)

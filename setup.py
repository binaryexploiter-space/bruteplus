from setuptools import setup
from setuptools.command.install import install
import os
import stat
import shutil

class CustomInstallCommand(install):
    def run(self):
        install.run(self)

        src_file = os.path.join(os.getcwd(), 'bruteplus')
        dest_file = '/usr/local/bin/bruteplus'

        print(f'[+] Installing bruteplus to {dest_file} ...')

        # Copy file to /usr/local/bin
        shutil.copyfile(src_file, dest_file)

        # Make it executable for all users
        os.chmod(dest_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

        print('[+] Installation completed!')
        print('[*] You can now run the tool using: bruteplus')

setup(
    name='bruteplus',
    version='2.1',
    description='Hydra & WPScan Command Generator and Runner',
    author='Oshan Ravindu',
    scripts=['bruteplus'],
    cmdclass={
        'install': CustomInstallCommand,
    }
)

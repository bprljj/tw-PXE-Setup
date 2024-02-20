

#!/usr/bin/env python3

import subprocess
import os

def main():
    # Change directory to where the make command needs to be executed
    os.chdir("/home/pxe/apps/ipxe-1.20.1/src")

    # Execute compilation command
    subprocess.run(["make", "bin-x86_64-efi/ipxe.efi", "EMBED=anil.ipxe"])

    # Copy the compiled file to the TFTP directory
    subprocess.run(["cp", "bin-x86_64-efi/ipxe.efi", "/var/lib/tftpboot/"])

    # Restart the TFTP server
    subprocess.run(["sudo", "systemctl", "restart", "tftp"])

if __name__ == "__main__":
    main()


import subprocess
import os

def install_packages(packages):
    print("Installing required packages...")
    command = ["yum", "install", "-y"]
    command.extend(packages)
    subprocess.run(command, check=True)

def install_python3():
    print("Installing Python 3...")
    install_packages(["python3"])

def install_development_tools():
    print("Installing development tools...")
    install_packages(["@development"])

def install_kernel_headers():
    print("Installing kernel headers...")
    install_packages(["kernel-headers"])

def install_numactl():
    print("Installing numactl...")
    install_packages(["numactl"])

def install_dpdk():
    print("Installing DPDK...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([os.path.join(current_dir, "install_dpdk.sh")], check=True)

def install_rdma():
    print("Installing RDMA...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([os.path.join(current_dir, "install_rdma.sh")], check=True)

def main():
    try:
        install_python3()
        install_development_tools()
        install_kernel_headers()
        install_numactl()
        install_dpdk()
        install_rdma()
        print("Installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Installation failed.")

if __name__ == "__main__":
    main()


import os
import sys
import subprocess

REQUIREMENTS_FILE = "requirements.txt"
LOG_FILE = "install.log"

def install_build_tools():
    """Downloads and installs Microsoft C++ Build Tools via PowerShell."""
    print("Downloading Microsoft C++ Build Tools...")
    
    # Download the installer
    subprocess.run([
        "powershell", "-Command",
        "Invoke-WebRequest -Uri https://aka.ms/vs/17/release/vs_BuildTools.exe -OutFile vs_BuildTools.exe"
    ], check=True)
    
    print("Installing Microsoft C++ Build Tools...")
    
    # Run the installer with silent arguments
    subprocess.run([
        "powershell", "-Command",
        "Start-Process -FilePath vs_BuildTools.exe -ArgumentList '--quiet --norestart --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended' -Wait"
    ], check=True)

    print("Installation complete.")

if __name__ == "__main__":
    install_build_tools()


def check_python():
    """Ensure Python is installed and meets version requirements."""
    required_major = 3
    required_minor = 9

    current_major = sys.version_info.major
    current_minor = sys.version_info.minor

    if (current_major, current_minor) < (required_major, required_minor):
        print(f"Python {current_major}.{current_minor} detected. Python {required_major}.{required_minor} or later is required.")
        sys.exit(1)

def check_build_tools():
    """Check if Microsoft C++ Build Tools are installed."""
    print("Checking for Microsoft C++ Build Tools...")
    result = subprocess.run(["where", "cl"], capture_output=True, text=True)

    if "could not be found" in result.stdout:
        print("\nMicrosoft C++ Build Tools are missing.")
        print("Please install them manually using the following steps:")
        print("1. Download the installer: https://aka.ms/vs/17/release/vs_BuildTools.exe")
        print("2. Run the installer and select 'C++ Build Tools'.")
        print("3. Ensure 'Windows 10 SDK' and 'MSVC v142' are selected.")
        print("4. Restart your terminal after installation.")
        sys.exit(1)

def create_virtual_env():
    """Create and activate a virtual environment."""
    venv_dir = "tts_env"
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    
    # Activate virtual environment
    if sys.platform == "win32":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
    
    return activate_script

def install_dependencies():
    """Install dependencies and log errors."""
    try:
        print("Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE], check=True)
        print("Installation complete.")
    except subprocess.CalledProcessError as e:
        with open(LOG_FILE, "w") as log:
            log.write(str(e))
        print(f"Installation failed. Check {LOG_FILE} for details.")
        sys.exit(1)

def main():
    """Run the setup process."""
    check_python()
    check_build_tools()
    activate_script = create_virtual_env()
    
    print(f"To activate the environment, run: {activate_script}")
    install_dependencies()

if __name__ == "__main__":
    main()

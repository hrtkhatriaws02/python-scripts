import subprocess

result = subprocess.run(
    [r"C:\Users\HimanshuKhatri\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\vermin.exe", "--no-tips", "."],
    capture_output=True,
    text=True
)

print("Vermin Output:\n")
print(result.stdout)

if result.stderr:
    print("Errors:\n", result.stderr)

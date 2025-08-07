from pathlib import Path

path = Path(r'C:\Users\JanezKoncilija\OneDrive - Axlhub\Py\Python_CC\pi_digits.txt')
#path = Path("pi_digits.txt")
contents = path.read_text()
print(contents)
file_path = r"C:\Path\To\File.hexhex"

with open(file_path, "r", encoding="utf-8") as f:
    hex_text = f.read()

import re
hex_text = re.sub(r'[^0-9A-Fa-f]', '', hex_text)
                           
byte_data = bytes.fromhex(hex_text)

print("Binary representation:")
for b in byte_data:
    print(f"{b:08b}", end=" ")
print("\n")

ascii_str = "".join(chr(b) if 32 <= b <= 126 else "." for b in byte_data)
print("ASCII representation (non-printable shown as .):")
print(ascii_str)


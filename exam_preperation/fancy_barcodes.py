import re

number_of_barcodes = int(input())

pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"


for _ in range(number_of_barcodes):
    barcode = input()
    valid_barcode = re.search(pattern, barcode)
    if valid_barcode:
        second_pattern = r"[0-9]+"
        have_number = re.search(second_pattern, barcode)
        if not have_number:
            print("Product group: 00")
        else:
            all_numers = re.findall(second_pattern, barcode)
            print(f'Product group: {"".join(all_numers)}')


    else:
        print("Invalid barcode")


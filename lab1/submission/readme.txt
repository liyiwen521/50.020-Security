# To test shift cipher in text mode
python3 shiftcipher_str.py -i sherlock.txt -o str_en.out -k 4 -m e
python3 shiftcipher_str.py -i str_en.out -o str_de.out -k 4 -m d

# To test shift cipher in binary mode
python3 shiftcipher_bin.py -i sherlock.txt -o bin_en.out -k 30 -m e
python3 shiftcipher_bin.py -i bin_en.out -o bin_de.out -k 30 -m d

# To decrypt flag
python3 decrypt_flag.py flag

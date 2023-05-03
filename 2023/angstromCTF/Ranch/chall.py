import string

f = open("flag.txt").read()

encrypted = ""

shift = int(open("secret_shift.txt").read().strip())

for i in f:
    if i in string.ascii_lowercase:
        encrypted += chr(((ord(i) - 97 + shift) % 26)+97)
    else:
        encrypted += i

print(encrypted)

#rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}
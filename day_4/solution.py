req_count = valid_count = 0
lines = ""
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def check_valid(lines_dict):
    valid_byr = 1920 <= int(lines_dict['byr']) <= 2020
    valid_iyr = 2010 <= int(lines_dict['iyr']) <= 2020
    valid_eyr = 2020 <= int(lines_dict['eyr']) <= 2030
    valid_hgt = ('cm' in lines_dict['hgt'] and 150 <= int(lines_dict['hgt'][0:-2]) <= 192) or \
                ('in' in lines_dict['hgt'] and 59 <= int(lines_dict['hgt'][0:-2]) <= 76)
    valid_hcl = ('#' == lines_dict['hcl'][0] and len(lines_dict['hcl']) == 7)
    valid_ecl = any(lines_dict['ecl'] == x for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    valid_pid = len(lines_dict['pid']) == 9 and lines_dict['pid'].isdigit()
    return valid_byr & valid_iyr & valid_eyr & valid_hgt & valid_hcl & valid_ecl & valid_pid


with open("input.txt", 'r') as file:
    for line in file:
        if line == '\n':
            lines = lines.replace("\n", "").strip().split(" ")
            lines_dict = {x.split(':')[0]: x.split(':')[1] for x in lines}
            diff = required_fields.difference(set(lines_dict.keys()))
            if len(diff) == 0:
                req_count += 1
                valid_count += int(check_valid(lines_dict))
            lines = ""
        else:
            lines += ' ' + line
print(req_count + 1)
print(valid_count + 1)

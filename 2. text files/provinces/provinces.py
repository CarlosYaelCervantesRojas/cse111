def main():
    list = make_list('provinces.txt')

    list.pop(0)
    list.pop()

    replace_ab(list)
    print(list)
    # count = times_ab(list)
    count = list.count('Alberta')
    print(f'\nAlberta occurs {count} times in the modified list.')

    
def make_list(filename):
    provinces_list = []
    with open(filename) as provinces_file:
        for row in provinces_file:
            clean_line = row.strip()
            provinces_list.append(clean_line)
    return provinces_list

def replace_ab(list):
    # for i in range(len(list)):
    #     if list[i] == 'AB':
    #         list[i] = 'Alberta'
    for province in list:
        if province == 'AB':
            i = list.index(province)
            list[i] = 'Alberta'

# def times_ab(list):
#     count = 0
#     for province in list:
#         if province == 'Alberta':
#             count += 1
#     return count

if __name__ == "__main__":
    main()
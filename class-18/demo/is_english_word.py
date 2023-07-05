# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV`
# MAX JEING MNDUE OHB
# THE QUICK BROWN FOX
# PDA LDINE LODOE MUD

from corpus_loader import word_list, name_list

# print(name_list)


# sentence: 'The quick brown fox jumped over the lazily sleeping dog'
def find_word(sentence):
    for word in sentence.split():
        if word in word_list:
            print(f'{word} It is here')
        else:
            print(f'{word} Nope,not here')


if __name__ == '__main__':
    find_word('IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV')

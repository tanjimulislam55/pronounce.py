# import PySimpleGUI as sg
class Pronounce():

    def __init__(self, word):
        self.word = word
        self.vowels = 'aeiou'

    def pronounce(self):        
        # splitting words into list though there is one word
        if '-' not in self.word:
            temp = self.word.split(" ")
        else:
            temp = self.word.split("-")
        # for more than one word
        if len(temp) > 1:
            for tmp in temp:
                self.per_word(tmp.lower())
        # for one word
        else:
            self.per_word(''.join(temp).lower())

    def per_word(self, tmp):
        to_del_char_index = 0
        consecutive_char = ' '
        previous_char = ' '
        # checking consecutive chars
        for index, value in enumerate(tmp):
            if value == previous_char:
                to_del_char_index = index
                consecutive_char = value
                break
            previous_char = value 
        # passing consecutive vowels
        if consecutive_char in self.vowels:
            print(''.join(self.match_spell(self.del_consc_vowel_char(tmp, consecutive_char, to_del_char_index))))
            # result = (''.join(self.match_spell(self.del_consc_vowel_char(tmp, consecutive_char, to_del_char_index))))
        else:
            print(''.join(self.match_spell(tmp)))
        #     result = (''.join(self.match_spell(tmp)))
        # form = sg.FlexForm('display pronounciation with GUI')
        # layout = [[sg.Text('Enter your name'), sg.InputText(result)], [sg.OK()]]
        # # button, (name,) = form.LayoutAndRead(layout)
        # button, (name,) = form.Layout(layout).Read()

    def del_consc_vowel_char(self, tmp, consecutive_char, to_del_char_index):
        res_str = [tmp[i] for i in range(len(tmp)) if i != to_del_char_index]
        if consecutive_char == 'e':
            res_str[to_del_char_index-1] = 'i'
        if consecutive_char == 'o':
            res_str[to_del_char_index-1] = 'u'
        return ''.join(res_str)

    def match_spell(self, word):
        borno_dict = {
            'q': 'ক', 
            'w': 'ও', 
            'e': 'এ', 
            'r': 'র', 
            't': 'ত', 
            'y': 'য়', 
            'u': 'উ', 
            'i': 'ই', 
            'o': 'ও', 
            'p': 'প', 
            'a': 'আ', 
            's': 'স', 
            'd': 'দ', 
            'f': 'ফ', 
            'g': 'গ', 
            'h': 'হ', 
            'j': 'জ', 
            'k': 'ক', 
            'l': 'ল', 
            'z': 'য', 
            'x': 'য', 
            'c': 'চ', 
            'v': 'ভ', 
            'b': 'ব', 
            'n': 'ন', 
            'm': 'ম', 
        }
        bn_word = []
        if word[0] in self.vowels:
            # splitting out first vowel
            splitted_word = word[1:]
        else:
            splitted_word = word[:]

        # for the first char
        for k, v in borno_dict.items():
            if word[0] == k and k in self.vowels:
                bn_word.append(borno_dict[k])
                break

        # stores consonants before vowel
        previous_char = ''
        for char in splitted_word:
            if char in self.vowels:
                if len(previous_char) == 2:
                    if previous_char == 'sh':
                        bn_word.append(self.kar(previous_char, char))
                        previous_char = ''
                    elif previous_char == 'kh':
                        bn_word.append(self.kar(previous_char, char))
                        previous_char = ''
                    else:
                        bn_word.append(self.kar(previous_char[0], char=''))
                        bn_word.append(self.kar(previous_char[1], char))
                        previous_char = ''
                elif len(previous_char) == 1:
                    bn_word.append(self.kar(previous_char, char))
                    previous_char = ''
            else:
                previous_char += char

        # for the last char
        for k,v in borno_dict.items():
            if word[-1] == k and k not in self.vowels:
                bn_word.append(borno_dict[k])   
                break

        return bn_word


    def kar(self, previous_char, char):
        bn_char = ' '
        kar_dict = {
            'qa': 'কা',
            'wa': 'ওয়া',
            'ra': 'রা',
            'ta': 'তা',
            'ya': 'য়া',
            'pa': 'পা',
            'sa': 'সা',
            'da': 'দা',
            'fa': 'ফা',
            'ga': 'গা',
            'ha': 'হা',
            'ja': 'জা',
            'ka': 'কা',
            'la': 'লা',
            'za': 'যা',
            'xa': 'যা',
            'cha': 'চা',
            'va': 'ভা',
            'ba': 'বা',
            'na': 'না',
            'ma': 'মা',
            'qe': 'কে',
            'we': 'ওয়ে',
            're': 'রে',
            'te': 'তে',
            'ye': 'য়ে',
            'pe': 'পে',
            'se': 'সে',
            'de': 'দে',
            'fe': 'ফে',
            'ge': 'গে',
            'he': 'হে',
            'je': 'জে',
            'ke': 'কে',
            'le': 'লে',
            'ze': 'যে',
            'xe': 'যে',
            'che': 'চে',
            've': 'ভে',
            'be': 'বে',
            'ne': 'নে',
            'me': 'মে',
            'qi': 'কি',
            'wi': 'ওই',
            'ri': 'রি',
            'ti': 'তি',
            'yi': 'য়ি',
            'pi': 'পি',
            'si': 'সি',
            'di': 'দি',
            'fi': 'ফি',
            'gi': 'গি',
            'hi': 'হি',
            'ji': 'জি',
            'ki': 'কি',
            'li': 'লি',
            'zi': 'যি',
            'xi': 'যি',
            'chi': 'চি',
            'vi': 'ভি',
            'bi': 'বি',
            'ni': 'নি',
            'mi': 'মি',
            'qo': 'কো',
            'wo': 'ওও',
            'ro': 'রো',
            'to': 'তো',
            'yo': 'য়ো',
            'po': 'পো',
            'so': 'সো',
            'do': 'দো',
            'fo': 'ফো',
            'go': 'গো',
            'ho': 'হো',
            'jo': 'জো',
            'ko': 'কো',
            'lo': 'লো',
            'zo': 'যো',
            'xo': 'যো',
            'cho': 'চো',
            'vo': 'ভো',
            'bo': 'বো',
            'no': 'নো',
            'mo': 'মো',
            'qu': 'কু',
            'wu': 'উ',
            'ru': 'রু',
            'tu': 'তু',
            'yu': 'য়ু',
            'pu': 'পু',
            'su': 'সু',
            'du': 'দু',
            'fu': 'ফু',
            'gu': 'গু',
            'hu': 'হু',
            'ju': 'জু',
            'ku': 'কু',
            'lu': 'লূ',
            'zu': 'যু',
            'xu': 'যু',
            'chu': 'চু',
            'vu': 'ভু',
            'bu': 'বু',
            'nu': 'নু',
            'mu': 'মু',

            'qqa': 'ককা',
            'qqe': 'ককে',
            'qqi': 'ক্কি',
            'qqo': 'ককো', 
            'qqu': 'ককু', 
            'wwa': 'য়া', 
            'wwe': 'য়ে', 
            'wwi': 'য়ি',  
            'wwo': 'য়ো', 
            'wwu': 'য়ু', 
            'rra': 'ররা',
            'rre': 'ররে',
            'rri': 'ররি',
            'rro': 'ররো',
            'rru': 'ররু', 
            'tta': 'ত্তা', 
            'tte': 'ত্তে', 
            'tti': 'ত্তি',  
            'tto': 'ত্তো', 
            'ttu': 'ত্তু', 
            'ppa': 'প্পা', 
            'ppe': 'প্পে', 
            'ppi': 'প্পি', 
            'ppo': 'প্পো', 
            'ppu': 'প্পু',
            'ssa': 'স্যা',
            'sse': 'স্যে', 
            'ssi': 'সসি',
            'sso': 'সসো', 
            'ssu': 'স্যু',
            'ffa': 'ফফা', 
            'ffe': 'ফফে', 
            'ffi': 'ফফি', 
            'ffo': 'ফফো',
            'ffu': 'ফফু',
            'gga': 'জ্ঞা', 
            'gge': 'জ্ঞে',
            'ggi': 'জ্ঞি', 
            'ggo': 'জ্ঞো', 
            'ggu': 'জ্ঞু',
            'hha': 'হহা', 
            'hhe': 'হহে', 
            'hhi': 'হহি', 
            'hho': 'হহো', 
            'hhu': 'হহু', 
            'jja': 'জ্জা', 
            'jje': 'জ্জে', 
            'jji': 'জ্জি', 
            'jjo': 'জ্জো',
            'jju': 'জ্জু', 
            'kka': 'ক্কা', 
            'kke': 'ক্কে', 
            'kki': 'ক্কি', 
            'kko': 'ক্কো', 
            'kku': 'ক্কু', 
            'lla': 'ল্লা', 
            'lle': 'ল্লে', 
            'lli': 'ল্লি',
            'llo': 'ল্লো', 
            'llu': 'ল্লু', 
            'zza': 'যযা', 
            'zze': 'যযে', 
            'zzi': 'যযি', 
            'zzo': 'যযো', 
            'zzu': 'যযু', 
            'cca': 'চ্চা', 
            'cce': 'চ্চে', 
            'cci': 'চ্চি', 
            'cco': 'চ্চো', 
            'ccu': 'চ্চু', 
            'vva': 'ভ্যা', 
            'vve': 'ভভে', 
            'vvi': 'ভভি', 
            'vvo': 'ভভো', 
            'vvu': 'ভভু', 
            'bba': 'ব্বা', 
            'bbe': 'ব্বে', 
            'bbi': 'ব্বি', 
            'bbo': 'ব্বো', 
            'bbu': 'ব্বু', 
            'nna': 'ন্না', 
            'nne': 'ন্নে', 
            'nni': 'ন্নি', 
            'nno': 'ন্নো', 
            'nnu': 'ন্নু', 
            'mma': 'ম্মা', 
            'mme': 'ম্মে',  
            'mmi': 'ম্মি', 
            'mmo': 'ম্মো', 
            'mmu': 'ম্মু',

            'q': 'ক',
            'w': 'ও',
            'e': 'এ',
            'r': 'র',
            't': 'ত',
            'y': 'য়',
            'u': 'উ',
            'i': 'ই',
            'o': 'ও',
            'p': 'প',
            'a': 'আ',
            's': 'স',
            'd': 'দ',
            'f': 'ফ',
            'g': 'গ',
            'h': 'হ',
            'j': 'জ',
            'k': 'ক',
            'l': 'ল',
            'z': 'য',
            'x': 'য',
            'c': 'চ',
            'v': 'ভ',
            'b': 'ব',
            'n': 'ন',
            'm': 'ম',

            'sha': 'শা',
            'she': 'শে',
            'shi': 'শি',
            'sho': 'শো',
            'shu': 'শু',
            'kha': 'খা',
            'khe': 'খা',
            'khi': 'খে',
            'kho': 'খো',
            'khu': 'খু',
            'tra': '',
            'tre': '',
            'tri': '',
            'tro': '',
            'tru': '',
            
        }
        for k, v in kar_dict.items():
            if (previous_char+char) == k:
                bn_char = kar_dict[k]
        return bn_char



if __name__ == "__main__":
    word = input('input word: ')
    p = Pronounce(word)
    p.pronounce()

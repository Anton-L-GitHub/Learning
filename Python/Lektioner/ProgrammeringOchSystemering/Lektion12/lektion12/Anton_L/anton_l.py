class Personnummer:

    def check_personnummer(personnummer):
        '''Returnerar om personnummer är korrekt eller ej'''
        try:
            assert isinstance(personnummer, str)
            personnummer = Personnummer._personnmr_formatter(personnummer)
            last_number = Personnummer._last_number(personnummer)
            if len(personnummer) <= 9:
                return f'Du glömde visst sista siffran! Men lugn! Kan det vara {last_number}? \nPersonnummer: {personnummer}{last_number}'
            elif personnummer[-1] != str(last_number):
                return f'Nehe du! Försök inte luras! :('
            elif personnummer[-1] == str(last_number):
                return f'Personnummret är korrekt'
        except AssertionError:
            raise f'Ange personnummer som en string!! {e} '

    def _personnmr_formatter(p_numb):
        '''Returnerar personnummer i 10siffror utan "-"'''
        try:
            p_numb = p_numb.replace('-', '')
            assert len(p_numb) < 14 or len(p_numb) < 9, 'Fel antal siffror!!'
            if len(p_numb) >= 11:
                return p_numb[2:]
            else:
                return p_numb
        except Exception as e:
            raise f'Value error! {e} '

    def _last_number(p_numb):
        '''Retunerar sista nummret i personnumret'''
        try:
            p_numb = p_numb if len(p_numb) <= 9 else p_numb[:-1]
            print(p_numb)
            total = []
            for i, num in enumerate(p_numb):
                num = int(num)
                if i % 2 == 0:
                    num *= 2
                    if num >= 10:
                        total.append(sum([int(i) for i in str(num)]))
                    else:
                        total.append(num)
                else:
                    total.append(num)
            return (10 - (sum(total) % 10)) % 10
        except ValueError as v:
            raise 'Fel input! Troligen kom något som inte var en siffra med'


personnummer = Personnummer.check_personnummer(input('Ange personnummer: '))
print(personnummer)

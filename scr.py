import glob

def obrazek_location(line):
    location = line
    location = location.strip('\n')
    location = location.replace('[/img]','')
    location = location.replace('[img]','')
    location = location.replace('[IMG]','')
    location = location.replace('[/IMG]','')
    location = location.replace(' ','')
    #location = location[5:-6]
    return location

def czyObrazek(line):
    if line[0:5]=="[img]" or line [0:5]=="[IMG]":
        return True
    else:
        return False

with open('Baza.html','w', newline='', encoding='latin-1') as wynFile:
    with open('style.css','w', newline='', encoding='latin-1') as cssFile:
        css =""".nazwaPytania{font-style: italic;font-size: 0.7em;}
        \n.pytanie\n{margin-top: 1.5em;border: 1px;border-style: dotted;border-color: black;padding: 0.5em;}
        \n.tresc_pytania\n{font-weight: bold;margin-bottom: 1.5em;}
        \n.dobra_odpowiedz\n{color: green;text-decoration: underline;}
        \n.dobra_odpowiedz img {border: 2px; border-color: green; border-style: solid;}
        \n.zla_odpowiedz\n{}
        \n.zla_odpowiedz img {filter: blur(0.05rem);}
        """
        cssFile.write(css)
    wynFile.write('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="latin-1"><title>Baza pytan</title><link rel="stylesheet" type="text/css" href="style.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><body>')

    for filepath in glob.iglob('baza/*.txt'):
        with open(filepath, 'r', newline='\n', encoding='latin-1') as pytanieFile:
            lin=0
            wynFile.write('<div class="pytanie"><div class="nazwaPytania">'+ filepath.strip('baza/') +'</div>')
            for line in pytanieFile:
                dict=""
                if line[0]=='X':
                    dict = line[1:]
                    answKey=[]
                    for x in range(1,len(dict)) :
                        if line[x] == '1':
                            answKey.append(int(x)+1)
                    #print(answKey)
                else:
                    if lin==1:
                        if czyObrazek(line):
                            wynFile.write('<div class="tresc_pytania"><img src="baza\\'+ obrazek_location(line) +'" alt="'+ obrazek_location(line) +'"></div>\n')
                        else:
                            wynFile.write('<div class="tresc_pytania">' + line + "</div>\n")
                    else:
                        if lin in answKey:
                            if czyObrazek(line):
                                wynFile.write('<div class="dobra_odpowiedz"><img src="baza\\'+ obrazek_location(line) +'" alt="'+ obrazek_location(line) +'"></div>\n')
                            else:
                                wynFile.write('<div class="dobra_odpowiedz"><li>' + line + "</li></div>\n")
                        else:
                            if czyObrazek(line):
                                wynFile.write('<div class="zla_odpowiedz"><img src="baza\\'+ obrazek_location(line) +'" alt="'+ obrazek_location(line) +'"></div>\n')
                            else:
                                wynFile.write('<div class="zla_odpowiedz"><li>' + line + "</li></div>\n")
                lin+=1
            wynFile.write('</div>')

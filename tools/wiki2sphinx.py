#!/usr/bin/python

# Author: Julius Künzel <jk.kdedev@smartlab.uber.space>

import sys, os, re

outputdir = "Kdenlive-Manual"
skipnonen=True

locales={'aa': 'Afar',
'ab': 'Abkhazian',
'ae': 'Avestan',
'af': 'Afrikaans',
'ak': 'Akan',
'am': 'Amharic',
'an': 'Aragonese',
'ar': 'Arabic',
'as': 'Assamese',
'av': 'Avaric',
'ay': 'Aymara',
'az': 'Azerbaijani',
'ba': 'Bashkir',
'be': 'Belarusian',
'bg': 'Bulgarian',
'bh': 'Bihari',
'bi': 'Bislama',
'bm': 'Bambara',
'bn': 'Bengali',
'bo': 'Tibetan',
'br': 'Breton',
'bs': 'Bosnian',
'ca': 'Catalan',
'ce': 'Chechen',
'ch': 'Chamorro',
'co': 'Corsican',
'cr': 'Cree',
'cs': 'Czech',
'cv': 'Chuvash',
'cy': 'Welsh',
'da': 'Danish',
'de': 'German',
'dz': 'Dzongkha',
'ee': 'Ewe',
'el': 'Greek',
'en': 'English',
'eo': 'Esperanto',
'es': 'Spanish',
'et': 'Estonian',
'eu': 'Basque',
'fa': 'Persian',
'ff': 'Fulah',
'fi': 'Finnish',
'fj': 'Fijian',
'fo': 'Faroese',
'fr': 'French',
'fy': 'Frisian',
'ga': 'Irish',
'gd': 'Gaelic',
'gl': 'Galician',
'gn': 'Guarani',
'gu': 'Gujarati',
'gv': 'Manx',
'ha': 'Hausa',
'he': 'Hebrew',
'hi': 'Hindi',
'ho': 'Hiri Motu',
'hr': 'Croatian',
'ht': 'Haitian',
'hu': 'Hungarian',
'hy': 'Armenian',
'hz': 'Herero',
'ia': 'Interlingua',
'id': 'Indonesian',
'ig': 'Igbo',
'ik': 'Inupiaq',
'io': 'Ido',
'is': 'Icelandic',
'it': 'Italian',
'iu': 'Inuktitut',
'ja': 'Japanese',
'jv': 'Javanese',
'ka': 'Georgian',
'kg': 'Kongo',
'kk': 'Kazakh',
'kl': 'Kalaallisut',
'km': 'Khmer',
'kn': 'Kannada',
'ko': 'Korean',
'kr': 'Kanuri',
'ks': 'Kashmiri',
'ku': 'Kurdish',
'kv': 'Komi',
'kw': 'Cornish',
'ky': 'Kyrgyz',
'la': 'Latin',
'lb': 'Luxembourgish',
'lg': 'Ganda',
'li': 'Limburgan',
'ln': 'Lingala',
'lo': 'Lao',
'lt': 'Lithuanian',
'lu': 'Luba-Katanga',
'lv': 'Latvian',
'mg': 'Malagasy',
'mh': 'Marshallese',
'mi': 'Maori',
'mk': 'Macedonian',
'ml': 'Malayalam',
'mn': 'Mongolian',
'mr': 'Marathi',
'ms': 'Malay',
'mt': 'Maltese',
'my': 'Burmese',
'na': 'Nauru',
'nb': 'Norwegian-Bokmal',
'nd': 'North Ndebele',
'ne': 'Nepali',
'ng': 'Ndonga',
'nl': 'Dutch',
'nn': 'Norwegian-Nynorsk',
'no': 'Norwegian',
'nr': 'South-Ndebele',
'nv': 'Navajo',
'ny': 'Nyanja',
'oc': 'Occitan',
'oj': 'Ojibwa',
'om': 'Oromo',
'or': 'Oriya',
'os': 'Ossetian',
'pa': 'Panjabi',
'pi': 'Pali',
'pl': 'Polish',
'ps': 'Pushto',
'pt': 'Portuguese',
'qu': 'Quechua',
'rn': 'Rundi',
'ro': 'Romanian',
'ru': 'Russian',
'rw': 'Kinyarwanda',
'sa': 'Sanskrit',
'sc': 'Sardinian',
'sd': 'Sindhi',
'se': 'Northern Sami',
'sg': 'Sango',
'si': 'Sinhalese',
'sk': 'Slovak',
'sl': 'Slovenian',
'sm': 'Samoan',
'sn': 'Shona',
'so': 'Somali',
'sq': 'Albanian',
'sr': 'Serbian',
'ss': 'Swati',
'st': 'Southern Sotho',
'su': 'Sundanese',
'sv': 'Swedish',
'sw': 'Swahili',
'ta': 'Tamil',
'te': 'Telugu',
'tg': 'Tajik',
'th': 'Thai',
'ti': 'Tigrinya',
'tk': 'Turkmen',
'tl': 'Tagalog',
'tn': 'Tswana',
'to': 'Tonga',
'tr': 'Turkish',
'ts': 'Tsonga',
'tt': 'Tatar',
'tw': 'Twi',
'ty': 'Tahitian',
'uk': 'Ukrainian',
'ur': 'Urdu',
'uz': 'Uzbek',
've': 'Venda',
'vi': 'Vietnamese',
'vo': 'Volapük',
'wa': 'Walloon',
'wo': 'Wolof',
'xh': 'Xhosa',
'yi': 'Yiddish',
'yo': 'Yoruba',
'zh': 'Chinese',
'zu': 'Zulu'}

def page_get_title(page):
    return re.search("(?<=<title>)([\s\S]*?)(?=<\/title>)", page)

def page_get_name(page):
    title = page_get_title(page)
    if title:
        title = title.group().split("/")
        if title[-1] in locales:
            return title[-2] + "-" + title[-1]
        else:
            return title[-1]
    else:
        return False

def page_is_english(page):
    title = page_get_title(page)
    if title:
        title = title.group().split("/")
        return title[-1] not in locales
    else:
        return False

def page_get_path(page):
    title = page_get_title(page)
    if title:
        title = title.group().split("/")
        if len(title) > 1 and "Kdenlive" in title:
            title.remove("Kdenlive")
        if len(title) > 1 and "Manual" in title:
            title.remove("Manual")
        if len(title) > 1:
            if title[-1] in locales:
                if len(title) < 3:
                    return outputdir;
                else:
                    title.pop(-1)
            title.pop(-1)
            return outputdir + "/" + "/".join(title)
        else:
            return outputdir
    else:
        return outputdir

def replace_regex(content, regex, replacement):
    such=re.compile(regex, re.DOTALL)
    for match in such.findall(content):
        content=content.replace(match, replacement)
    return content

def reformat_content(content):

    # remove [[Category:Kdenlive]]
    content = content.replace('[[Category:Kdenlive]]', '')

    # remove side switcher
    content=replace_regex(content, '{{Prevnext2[\s\S]*?}}', '')

    # replace new line sequence
    content = content.replace('&lt;br&gt;', '\n')

    # remove translation patterns
    content=replace_regex(content, '&lt;!--T:.*?--&gt;', '')
    content=content.replace('&lt;languages/&gt;\n', '')
    content=content.replace('&lt;translate&gt;\n', '')
    content=content.replace('&lt;/translate&gt;', '')
    content=content.replace('Special:myLanguage/', '')

    # {{#ev:youtube|bMwbffYIS40}}

    # [[Kdenlive/Manual/Effects/Alpha manipulation/Color Selection|Colour Selection]]

    #

    # reduce blank line
    content=replace_regex(content, '\n{4,}', '\n\n\n')

    return content


def page_get_content(page):
    content = re.search("(?<=<text)([\s\S]*?)(?=<\/text>)", page)
    if content:
        return re.search("(?<=>)([\s\S]*)", content.group())
    else:
        return False


if len(sys.argv) != 2:
    sys.exit('you must specify a file to parse!')
inputfile=sys.argv[1]
if not os.path.isfile(inputfile):
    sys.exit('input file %s not found' %inputfile)
text=open(inputfile,"r").read()

pages = re.split("(?<=<page>)([\s\S]*?)(?=<\/page>)", text)

for page in pages:

    if not page_get_title(page):
        pages.remove(page)

for page in pages:

    if skipnonen and page_is_english(page):
        path = page_get_path(page)
        if not os.path.isdir(path):
            os.makedirs(path)
        content = page_get_content(page)
        if content:
            content = reformat_content(content.group())
            f = open(path + "/" + page_get_name(page) + ".rst", "w")
            f.write(content)
            f.close()

print("Successfully wrote %d files to dir %s" %(len(pages), outputdir))

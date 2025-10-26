#!/usr/bin/python

# Author: Julius Künzel <jk.kdedev@smartlab.uber.space>

import sys, os, re
import subprocess
import json


outputdir = "Kdenlive-Manual"
skipnonen=True
showwarnings=False
fetchauthors=True

wikifiles = []
globalwarnings = []
allauthors = {''}

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
'pt-br': 'Brazilian Portuguese',
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
'zh-cn': 'Chinese (Simplified)',
'zh-hans': 'Chinese (Simplified)',
'zh-tw': 'Chinese (Taiwan))',
'zh-hant': 'Chinese (Traditional)',
'zu': 'Zulu'}

def page_get_raw_title(page):
    title = re.search("(?<=<title>)([\s\S]*?)(?=<\/title>)", page)
    if title:
        return title.group()
    else:
        return False

def page_get_title(page):
    title = page_get_raw_title(page)
    if title:
        return title.casefold().replace(' ', '_')
    else:
        return False

def page_get_name(page):
    title = page_get_title(page)
    if title:
        title = title.split("/")
        if title[-1] in locales:
            return title[-2] + "-" + title[-1]
        else:
            return title[-1]
    else:
        return False

def page_is_english(page):
    title = page_get_title(page)
    if title:
        title = title.split("/")
        return title[-1] not in locales
    else:
        return False

def page_get_path(page):
    title = page_get_title(page)
    if title:
        title = title.split("/")
        if len(title) > 1 and "kdenlive" in title:
            title.remove("kdenlive")
        if len(title) > 1 and "manual" in title:
            title.remove("manual")
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

def page_get_authors(page):
    authors = []
    if not fetchauthors:
        return False
    title = page_get_raw_title(page)
    url = 'https://userbase.kde.org/api.php?action=query&prop=contributors&format=json&pclimit=max&titles=%s' %title
    result = subprocess.run(['wget', '-qO-', url], stdout=subprocess.PIPE)
    #print(str(result.stdout))
    contents = json.loads(str(result.stdout)[2:-1])
    if contents:
        pages = contents['query']['pages']
        for key in pages.keys():
            namedict =	{
                "Jlskuz": "Julius Künzel <jk.kdedev@smartlab.uber.space",
                "J-b-m": "Jean-Baptiste Mardelle <jb@kdenlive.org>",
                "Vpinon": "Vincent Pinon <vpinon@kde.org>",
                "Yurchor": "Yuri Chornoivan",
                "Granjow": "Simon Eugster <simon.eu@gmail.com>",
                "Merlimau": "Eugen Mohr",
                "Alund": "Anders Lund",
                "Ttill": "Till Theato <root@ttill.de>",
                "Camillemo": "Camille Moulin",
                "Claus chr": "Claus Christensen",
                "Ognarb": "Carl Schwan <carl@carlschwan.eu>"
            }
            for author in pages[key]['contributors']:
                if namedict.get(author['name']):
                    authors.append(namedict.get(author['name']))
                    allauthors.add(namedict.get(author['name']))
                else:
                    authors.append('%s (https://userbase.kde.org/User:%s)' %(author['name'], author['name']))
                    allauthors.add('%s (https://userbase.kde.org/User:%s)' %(author['name'], author['name']))
    return authors

def remove_regex(content, regex):
    return re.sub(regex, '', content, flags=re.DOTALL | re.I)

def rewrite_admonition(content, w, s):
    res = re.compile('(?<=\{\{'+w+'\|)([\s\S]*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        if '2=' in match and '1=' in match:
            e = match.replace('1= ', '').replace('2= ', '').split('|')
            content = content.replace('{{'+w+'|%s}}' %match, '.. %s:: %s\n\n   %s\n' %(s, e[0], e[1]))
        else:
            lines = match.replace('1= ', '').split('\n')
            content = content.replace('{{'+w+'|%s}}' %match, '.. %s::\n\n   %s\n' %(s, '\n   '.join(lines)))
    return content

def rewrite_heading(content, level, surroundchar, linechar, first=False):
    surround = surroundchar
    while len(surround) < level:
        surround = surround + surroundchar
    res = re.compile('(?<=={'+str(level)+'})[^=\n]+?(?=={'+str(level)+'})', re.DOTALL)
    for match in res.findall(content):
        n = match
        while n.startswith(' '):
            n = n[1:]
        while n.endswith(' '):
            n = n[:-1]
        line = linechar
        while len(line) < len(n):
            line = line + linechar
        if first:
            replacement = '%s\n%s\n\n.. contents::\n\n' %(n, line)
            first = False
        else:
            replacement = '\n%s\n%s\n' %(n, line)
        content = content.replace('%s%s%s' %(surround, match, surround), replacement)
    return content

def rewrite_embedvideo(content, service, url):
    content = content.replace('{{#evp:%s' %service.casefold(), '{{#ev:%s' %service.casefold())

    res = re.compile('(?<=\{\{#ev:'+service.casefold()+'\|)(.*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        a = match.split('|')
        if len(a) > 3:
            content = content.replace('{{#ev:%s|%s}}' %(service.casefold() , match), '`%s(%s) <%s%s>`_' %(a[3], service, url, a[0]))
        else:
            content = content.replace('{{#ev:%s|%s}}' %(service.casefold() , match), '%s%s' %(url, a[0]))
    return content

def reformat_content(content, fullpath):
    warnings = []

    # rewrite code formatting (needs to be done first do avoid conflicts)
    res = re.compile('(?<=&lt;code&gt;&lt;nowiki&gt;)(.*?)(?=&lt;\/nowiki&gt;&lt;\/code&gt;)', re.DOTALL)
    for match in res.findall(content):
        r = match.replace('&lt;', '<').replace('&gt;', '>')
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('&lt;code&gt;&lt;nowiki&gt;%s&lt;/nowiki&gt;&lt;/code&gt;' %match, '``%s``' %r)

    res = re.compile('(?<=&lt;code&gt;)(.*?)(?=&lt;\/code&gt;)', re.DOTALL)
    for match in res.findall(content):
        r = match.replace('&lt;', '<').replace('&gt;', '>')
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('&lt;code&gt;%s&lt;/code&gt;' %match, '``%s``' %r)

    res = re.compile('(?<=&lt;nowiki&gt;)(.*?)(?=&lt;\/nowiki&gt;)', re.DOTALL)
    for match in res.findall(content):
        r = match.replace('&lt;', '<').replace('&gt;', '>')
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('&lt;nowiki&gt;%s&lt;/nowiki&gt;' %match, '``%s``' %r)

    # rewrite input and output to code formatting
    for tag in ['Input','Output']:
        content = content.replace('{{%s|1=' %tag, '{{%s|' %tag)
        res = re.compile('(?<=\{\{'+tag+'\|)([\s\S]*?)(?=\}\})', re.DOTALL)
        for match in res.findall(content):
            lines = match.split('\n')
            r = '\n   '.join(lines)
            while r.startswith('``'):
                r = r[2:]
            while r.endswith('``'):
                r = r[:-2]

            content = content.replace('{{%s|%s}}' %(tag, match), '\n\n.. code-block:: bash\n\n   %s' %r)

    res = re.compile('(?<=&lt;syntaxhighlight lang="bash"&gt;\n)[\s\S]*?(?=&lt;/syntaxhighlight&gt;)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('&lt;syntaxhighlight lang="bash"&gt;\n%s&lt;/syntaxhighlight&gt;' %match, match)

    content=re.sub('vers*(ions)* &gt;=', 'version >=', content, flags=re.I)
    content=re.sub('vers*(ions)* &gt;', 'version >', content, flags=re.I)
    content=re.sub('vers*(ions)* &lt;=', 'version <=', content, flags=re.I)
    content=re.sub('vers*(ions)* &lt;', 'version <', content, flags=re.I)

    # remove [[Category:]]
    content=remove_regex(content, '\[\[Category:.*?\]\]\n*')

    # remove side switcher
    content=remove_regex(content, '{{Prevnext2[\s\S]*?}}')

    # replace new line sequence
    content=re.sub('&lt;br *.*/*&gt;', '\n', content, flags=re.I)
    content=remove_regex(content, '&lt;div class="clearfix"&gt;&lt;/div&gt;')

    # remove translation patterns
    content=remove_regex(content, '&lt;!--T:.*?--&gt;')
    content=remove_regex(content, '&lt;languages */&gt;\n*')
    content=remove_regex(content, '&lt;/*translate&gt;')
    content=remove_regex(content, 'Special:MyLanguage/')

    content=remove_regex(content, '&lt;div class="manualtoc"&gt;\n')
    content = remove_regex(content, '(&lt;\/div&gt;)\n*.*Contents page\n*}}\n*')

    content=remove_regex(content, '&lt;references */&gt;')

    content=remove_regex(content, '&lt;\!--\{*--\&gt;')
    content=remove_regex(content, '&lt;\!--\}*--\&gt;')

    content=remove_regex(content, '(&lt;span id=")(.*?)("&gt;&lt;\/span&gt;)')

    toplevel = 2
    while not re.search('(={'+str(toplevel)+'})[^=\n]+?(={'+str(toplevel)+'})[^=]', content) and toplevel < 8:
        toplevel = toplevel + 1

    content = rewrite_heading(content, toplevel + 3, '=', '^')
    content = rewrite_heading(content, toplevel + 2, '=', '~')
    content = rewrite_heading(content, toplevel + 1, '=', '-')
    content = rewrite_heading(content, toplevel, '=', '=', True)

    # rewrite todos to comments
    res = re.compile('(?<=\{\{:Kdenlive/Templates/ContentTodo\|\n)([\s\S]*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        lines = match.split('\n')
        content = content.replace('{{:Kdenlive/Templates/ContentTodo|\n'+match+'}}', '..\n   TODO:\n   '+'   '.join(lines) + '\n')
        warnings.append('[ ] TODO: %s' %' '.join(lines))

    # rewrite comments
    res = re.compile('(?<=&lt;!--)(.*?)(?=--&gt;)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('&lt;!--'+match+'--&gt;', '.. '+match)
        warnings.append('[ ] INFO: comment ' + match.replace('\n' , ' '))

    # rewrite file paths
    res = re.compile('(?<=&lt;tt&gt;)(.*?)(?=&lt;\/tt&gt;)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('&lt;tt&gt;%s&lt;/tt&gt;' %match, ':file:`%s`' %match)

    # rewrite keyboard sequences
    res = re.compile('(?<=&lt;keycap&gt;)(.*?)(?=&lt;\/keycap&gt;)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('&lt;keycap&gt;%s&lt;/keycap&gt;' %match, ':kbd:`%s`' %match)

    # rewrite paths
    res = re.compile('(?<=\{\{Path\|)([\s\S]*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('{{Path|%s}}' %match, ':file:` /%s`' %match)

    # rewrite icons
    res = re.compile('(?<=\{\{Icon\|)([\s\S]*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        wikifiles.append('Icon: %s.svg' %match)
        content = content.replace('{{Icon|%s}}' %match, '\n\n.. image:: /images/icons/%s.svg\n\n' %match)

    res = re.compile('(?<=\{\{Icon1\|)([\s\S]*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        wikifiles.append('Icon: %s' %match)
        content = content.replace('{{Icon1|%s}}' %match, '\n\n.. image:: /images/icons/%s\n\n' %match)

    # rewrite admonitions
    content = rewrite_admonition(content, 'Tip', 'tip')
    content = rewrite_admonition(content, 'Note', 'note')
    content = rewrite_admonition(content, 'Info', 'hint')
    content = rewrite_admonition(content, 'Remember', 'note')
    content = rewrite_admonition(content, 'Warning', 'warning')

    # rewrite bold line formatting
    res = re.compile('(?<=\'\'\')(.*?)(?=\'\'\')', re.DOTALL)
    for match in res.findall(content):
        r = match
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('\'\'\'%s\'\'\'' %match, '**%s**' %r)

    res = re.compile('(?<=&lt;b&gt;)(.*?)(?=&lt;\/b&gt;)', re.DOTALL)
    for match in res.findall(content):
        r = match
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('&lt;b&gt;%s&lt;/b&gt;' %match, '\n**%s**\n' %r)

    res = re.compile('(?<=\n;)(.*?)(?=\n)', re.DOTALL)
    for match in res.findall(content):
        r = match
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('\n;%s\n' %match, '\n**%s**\n' %r)

    # rewrite italic inline formatting
    res = re.compile('(?<=\'\')(.*?)(?=\'\')', re.DOTALL)
    for match in res.findall(content):
        r = match
        while r.startswith(' '):
            r = r[1:]
        while r.endswith(' '):
            r = r[:-1]
        content = content.replace('\'\'%s\'\'' %match, '*%s*' %r)


    # rewrite line indents
    res = re.compile('(?<=\n: )(.*?)(?=\n)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('\n: %s\n' %match, '\n   %s\n' %match)
    res = re.compile('(?<=\n:)(.*?)(?=\n)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('\n:%s\n' %match, '\n   %s\n' %match)

    # rewrite menu menuchoice
    res = re.compile('(?<=&lt;menuchoice&gt;)(.*?)(?=&lt;/menuchoice&gt;)', re.DOTALL)
    for match in res.findall(content):
        e = match.split(' -&gt; ')
        if not len(e) > 1:
            e = match.split('-&gt;')
        if len(e) > 1:
            content = content.replace('&lt;menuchoice&gt;%s&lt;/menuchoice&gt;' %match, ':menuselection:`%s`' %' --> '.join(e))
        else:
            content = content.replace('&lt;menuchoice&gt;%s&lt;/menuchoice&gt;' %match, ':menuselection:`%s`' %match)

    # rewrite embed video templates
    content = rewrite_embedvideo(content, 'YouTube', 'https://youtu.be/')
    content = rewrite_embedvideo(content, 'Vimeo', 'https://vimeo.com/')

    res = re.compile('(?<=\{\{#ev:)(.*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        print('==== ERROR: ev embed video with service %s that is not implemented yet – n file %s' %(match, fullpath))

    res = re.compile('(?<=\{\{#evp:)(.*?)(?=\}\})', re.DOTALL)
    for match in res.findall(content):
        print('==== ERROR: evp embed video with service %s that is not implemented yet – n file %s' %(match, fullpath))

    # rewrite wiki files
    for tag in ['File', 'file', 'Image']:
        res = re.compile('(?<=\[\['+tag+':).*?(?=\]\])', re.DOTALL)
        for match in res.findall(content):
            a = match.split('|')
            while a[0].startswith(' '):
                a[0] = a[0][1:]
            if '.mp4' in a[0]:
                warnings.append('[ ] WARNING: Video file %s (not supported by Sphinx)' %(a[0]))
                replacement = ' VIDEO FILE %s MISSING ' %a[0]
            elif '.zip' in a[0]:
                warnings.append('[ ] WARNING: Archive file %s (not supported by Sphinx)' %(a[0]))
                replacement = '` Archive File: %s <%s>`_  ' %(a[0], a[0])
            else:
                replacement = '\n\n.. image:: /images/%s' %a[0].replace(' ', '_')
                wikifiles.append(a[0])
                a.pop(0)
                for e in a:
                    while e.startswith(' '):
                        e = e[1:]
                    while e.endswith(' '):
                        e = e[:-1]
                    if re.search('^(center|left|right)$',e):
                        replacement = replacement + '\n   :align: '+e
                    elif re.search('^[0-9]+?(px)?$',e):
                        if not re.search('(em|ex|px|in|cm|mm|pt|pc)',e):
                            e = '%spx' %e
                        replacement = replacement + '\n   :width: '+e
                    elif not re.search('^(thumb|frame|frameless)$', e):
                        replacement = replacement + '\n   :alt: '+e
            content = content.replace('[[%s:%s]]' %(tag, match), '%s\n' %replacement)

    # [[a/b/c|xyz]]
    for tag in ['Kdenlive/Manual/', ' Kdenlive/Manual/', '']:
        res = re.compile('(?<=\[\['+tag+').*?\|.*?(?=\]\])', re.DOTALL)
        for match in res.findall(content):
            a = match.split('|')
            b = a[0].split('/')
            refname = b[-1].casefold()
            if '#' in refname:
                c = refname.split('#')
                refname = c[0]
            if a[1] and a[1].replace(' ', '_').casefold() != refname:
                #content = content.replace('[[%s%s]]' %(tag, match), ':ref:`%s<%s>`' %(refname.replace(' ', '_'), a[1]))
                #content = content.replace('[[%s%s]]' %(tag, match), '`%s`_' %refname)
                content = content.replace('[[%s%s]]' %(tag, match), ':ref:`%s`' %refname.replace(' ', '_'))
            else:
                #content = content.replace('[[%s%s]]' %(tag, match), ':ref:`%s`' % refname.replace(' ', '_'))
                #content = content.replace('[[%s%s]]' %(tag, match), '`%s`_' %refname)
                content = content.replace('[[%s%s]]' %(tag, match), ':ref:`%s`' %refname.replace(' ', '_'))


    # rewrite some specific links
    for tag in ['K3b', 'Kaffeine']:
        content = content.replace('[[%s]]' %tag, tag)

    # rewrite external links
    res = re.compile('(?<=\[)(http.*?)(?=\])', re.DOTALL)
    for match in res.findall(content):
        a = match.split(' ')
        if len(a) > 1:
            link = a[0]
            a.pop(0)
            name = ' '.join(a)
            while name.startswith(' '):
                name = name[1:]
            content = content.replace('[' + match + ']', '`%s <%s>`_' %(name, link))
        else:
            link = match
            content = content.replace('[' + match + ']', link)
        # check for old bugtracker
        if 'kdenlive.org/mantis' in link:
            warnings.append('[ ] WARNING: link old mantis bug tracker %s' %link)

    # rewrite unordered lists that miss the space between * and fist word
    res = re.compile('(?<=\n\*)(.*?)(?=\n)', re.DOTALL)
    for match in res.findall(content):
        if match.startswith(' '):
            continue
        content = content.replace('\n*%s\n' %match, '\n* %s\n' %match)

    # rewrite unordered lists
    j = 4
    while j > 0:
        blanks = ''
        while len(blanks) < (j*2-2):
            blanks = blanks + '  '
        hashtags = '#'
        while len(hashtags) < j:
            hashtags = hashtags + '#'
        res = re.compile('(?<=\n#{'+str(j)+'})(.*?)(?=\n)', re.DOTALL)
        for match in res.findall(content):
            e = match
            if not e.startswith(' '):
                e = ' %s'
            content = content.replace('\n%s%s\n' %(hashtags, match), '\n%s*%s\n' %(blanks, e))
        j = j - 1

    # tables (see effects.rst)
    res = re.compile('(?<={\|)[\s\S]*?(?=\|})', re.DOTALL)
    for match in res.findall(content):
        if 'class=' in match:
            tabcontent = re.search('\|-[\s\S]*', match)
            if not tabcontent:
                tabcontent = re.search('\|[\s\S]*', match)
                items = tabcontent.group().split('|')
                items = '\n'.join(items)
                content = content.replace('{|%s|}' %match, items)
                continue
            else:
                tabcontent = tabcontent.group()
            tabcontent = tabcontent.replace('\n\n\n', '\n')
            tabcontent = tabcontent.split('|-\n|')
            res = re.search('(?<=!).*?(?=\n)', match)
            col = 0
            if res:
                tabhead = res.group().split('!!')
                col = len(tabhead)
                table = '.. list-table::\n   :header-rows: 1\n\n   * - %s' %'\n     - '.join(tabhead)
            else:
                table = '.. list-table::\n'
            if not tabcontent[0]:
                tabcontent.pop(0)
            for row in tabcontent:
                cells = row.replace('\n', ' ')
                cells = cells.split('||')
                while col > 0 and len(cells) < col:
                    cells.append(' -')
                table = table + '\n   * - %s' %'\n     - '.join(cells)
            content = content.replace('{|%s|}' %match, table)
        else:
            items = match.split('|')
            items = '\n'.join(items)
            content = content.replace('{|%s|}' %match, items)

    # reduce blank line
    content=re.sub('\n{4,}', '\n\n\n', content)

    # rewrite footnotes
    footnotes = []
    res = re.compile('(?<=&lt;ref&gt;)(.*?)(?=&lt;\/ref&gt;)', re.DOTALL)
    for match in res.findall(content):
        footnotes.append('.. [%d] %s' %(len(footnotes)+1, match))
        content = content.replace('&lt;ref&gt;' + match + '&lt;/ref&gt;', ' [%d]_ ' %len(footnotes))

    for fn in footnotes:
        content = content + fn + '\n'

    # fix
    res = re.compile('(?<=\n\* \n)(.*?)(?=\n)', re.DOTALL)
    for match in res.findall(content):
        content = content.replace('\n* \n%s\n' %match, '\n* %s\n' %match)

    content = content.replace('&amp;rarr;', '>')
    content = content.replace('&amp;mdash;', '–')
    content = content.replace(' &amp;', ' & ')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = remove_regex(content, '(?<=\n)( )(?=.)')

    if '[[' in content and ']]' in content:
        print('==== ERROR: [[ and ]] still in file %s' %fullpath)

    if warnings:
        globalwarnings.append('**MESSAGES FOR FILE %s**\n' %fullpath)
        globalwarnings.append('\n'.join(warnings))
        globalwarnings.append('\n')

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

count = 0
for page in pages:
    if skipnonen and page_is_english(page):
        path = page_get_path(page)
        if 'user:' in path:
            continue
        if not os.path.isdir(path):
            os.makedirs(path)
        raw = page_get_content(page)
        if raw:

            fullpath = path + "/" + page_get_name(page) + ".rst"

            authors = page_get_authors(page)
            meta = '.. metadata-placeholder\n\n'
            if authors:
                print('processing page %d' %(count))
                meta = meta + '   :authors: - %s\n\n' %'\n             - '.join(authors)
            meta = meta + '   :license: Creative Commons License SA 4.0'

            content = '%s\n\n.. _%s:\n\n%s' %(meta, page_get_name(page).replace(' ','_').casefold(), reformat_content(raw.group(), fullpath))
            #content = '%s' %(reformat_content(raw.group(), fullpath))
            f = open(fullpath, "w")
            f.write(content)
            f.close()
            parentfolder = path.split('/')[-1]
            if parentfolder == outputdir:
                indexfile = outputdir + '/index.rst'
            else:
                indexfile = path+'.rst'
            if os.path.isfile(indexfile):
                f = open(indexfile, "r")
                if f.read().find('toctree')  > -1:
                    content = '   %s\n' %'/'.join(fullpath.replace(outputdir+'/', '').replace('.rst', '').split('/')[-2:])
                else:
                    content = '.. toctree::\n'
                    content = content + '   :caption: Contents:\n\n'
                    content = content + '   ' + '/'.join(fullpath.replace(outputdir+'/', '').replace('.rst', '').split('/')[-2:]) + '\n'
                f = open(indexfile, "a")
                f.write(content)
                f.close()
            else:
                content = 'Welcome to Kdenlive\'s documentation!\n'
                content = content + '====================================\n'
                content = content + '.. toctree::\n'
                content = content + '   :caption: Contents:\n\n'
                content = content + '   %s\n' %'/'.join(fullpath.replace(outputdir+'/', '').replace('.rst', '').split('/')[-2:])
                f = open(indexfile, "w")
                f.write(content)
                f.close()

            count = count + 1

if showwarnings:
    print('\n'.join(globalwarnings))
if globalwarnings:
    f = open('messages.md', "w")
    f.write('\n'.join(globalwarnings))
    f.close()
    print('Messages have been written to messages.md')
if wikifiles:
    f = open('wikifiles.txt', "w")
    f.write('\n'.join(wikifiles))
    f.close()
    print('Found %d (image) files that are not downloaded yet. You can find a list with filename in wikifiles.txt' %len(wikifiles))
if allauthors:
    f = open('authors.txt', "w")
    f.write('\n'.join(allauthors))
    f.close()
    print('Found %d authors. Names are written to authors.txt' %len(allauthors))
print("Successfully wrote %d files out of %d possible pages (skipped %d) to dir %s" %(count, len(pages), len(pages)-count, outputdir))

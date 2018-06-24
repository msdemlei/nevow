# Copyright (c) 2004 Divmod.
# See LICENSE for details.

"""Defines XHTML entities to make them easier to include in stan
trees.
"""

import types

from twisted.python import compat


__by_number = {}

def makeEntity(xxx_todo_changeme):
    (name, num, description) = xxx_todo_changeme
    from nevow.stan import Entity
    e = Entity(name, num, description)
    __by_number[types.IntType(num)] = e
    globals()[name] = e


def getEntity(num):
    if isinstance(num, (compat.unicode, bytes)):
        num = ord(num)
    return __by_number[num]


[makeEntity(ent) for ent in
[('nbsp', '160', 'non-breaking space'), ('cent', '162', 'cent sign '), ('pound', '163', 'pound sign'), ('curren', '164', 'currency sign'), ('yen', '165', 'yen sign'), ('brvbar', '166', 'broken vertical bar'), ('sect', '167', 'section sign'), ('uml', '168', 'diaeresis'), ('copy', '169', 'copyright sign'), ('ordf', '170', 'feminine ordinal indicator'), ('laquo', '171', 'left-pointing double angle quotation mark'), ('not', '172', 'not sign'), ('shy', '173', 'soft hyphen'), ('reg', '174', 'registered sign '), ('macr', '175', 'macron'), ('deg', '176', 'degree sign'), ('plusmn', '177', 'plus-minus sign'), ('sup2', '178', 'superscript two '), ('sup3', '179', 'superscript three'), ('acute', '180', 'acute accent'), ('micro', '181', 'micro signB5'), ('para', '182', 'pilcrow sign'), ('middot', '183', 'middle dot'), ('cedil', '184', 'cedilla'), ('sup1', '185', 'superscript one'), ('ordm', '186', 'masculine ordinal indicator'), ('raquo', '187', 'right-pointing double angle quotation mark'), ('frac14', '188', 'vulgar fraction one- quarter'), ('frac12', '189', 'vulgar fraction one- half'), ('frac34', '190', 'vulgar fraction three- quarters'), ('iquest', '191', 'inverted question mark'), ('Agrave', '192', 'Latin capital letter A with grave'), ('Aacute', '193', 'Latin capital letter A with acute'), ('Acirc', '194', 'Latin capital letter A with circumflex'), ('Atilde', '195', 'Latin capital letter A with tilde'), ('Auml', '196', 'Latin capital letter A with diaeresis'), ('Aring', '197', 'Latin capital letter A with ring above'), ('AElig', '198', 'Latin capital letter AE'), ('Ccedil', '199', 'Latin capital letter C with cedilla'), ('Egrave', '200', 'Latin capital letter E with grave'), ('Eacute', '201', 'Latin capital letter E with acute'), ('Ecirc', '202', 'Latin capital letter E with circumflex'), ('Euml', '203', 'Latin capital letter E with diaeresis'), ('Igrave', '204', 'Latin capital letter I with grave'), ('Iacute', '205', 'Latin capital letter I with acute'), ('Icirc', '206', 'Latin capital letter I with circumflex'), ('Iuml', '207', 'Latin capital letter I with diaeresis'), ('eth', '208', 'Latin capital letter eth'), ('Ntilde', '209', 'Latin capital letter N with tilde'), ('Ograve', '210', 'Latin capital letter O with grave'), ('Oacute', '211', 'Latin capital letter O with acute'), ('Ocirc', '212', 'Latin capital letter O with circumflex'), ('Otilde', '213', 'Latin capital letter O with tilde'), ('Ouml', '214', 'Latin capital letter O with diaeresis'), ('times', '215', 'multiplication sign'), ('Oslash', '216', 'Latin capital letter O with stroke'), ('Ugrave', '217', 'Latin capital letter U with grave'), ('Uacute', '218', 'Latin capital letter U with acute'), ('Ucirc', '219', 'Latin capital letter U with circumflex'), ('Uuml', '220', 'Latin capital letter U with diaeresis'), ('Yacute', '221', 'Latin capital letter Y with acute'), ('thorn', '222', 'Latin capital letter thorn'), ('szlig', '223', 'Latin small letter sharp'), ('agrave', '224', 'Latin small letter a with grave'), ('aacute', '225', 'Latin small letter a with acute'), ('acirc', '226', 'Latin small letter a with circumflex'), ('atilde', '227', 'Latin small letter a with tilde'), ('auml', '228', 'Latin small letter a with diaeresis'), ('aring', '229', 'Latin small letter a with ring above'), ('aelig', '230', 'Latin small letter ae'), ('ccedil', '231', 'Latin small letter c with cedilla'), ('egrave', '232', 'Latin small letter e with grave'), ('eacute', '233', 'Latin small letter e with acute'), ('ecirc', '234', 'Latin small letter e with circumflex'), ('euml', '235', 'Latin small letter e with diaeresis'), ('igrave', '236', 'Latin small letter i with grave'), ('iacute', '237', 'Latin small letter i with acute'), ('icirc', '238', 'Latin small letter i with circumflex'), ('iuml', '239', 'Latin small letter i with diaeresis'), ('eth', '240', 'Latin small letter eth'), ('ntilde', '241', 'Latin small letter n with tilde'), ('ograve', '242', 'Latin small letter o with grave'), ('oacute', '243', 'Latin small letter o with acute'), ('ocirc', '244', 'Latin small letter o with circumflex'), ('otilde', '245', 'Latin small letter o with tilde'), ('ouml', '246', 'Latin small letter o with diaeresis'), ('divide', '247', 'division  sign'), ('oslash', '248', 'Latin small letter o with stroke'), ('ugrave', '249', 'Latin small letter u with grave'), ('uacute', '250', 'Latin small letter u with acute'), ('ucirc', '251', 'Latin small letter u with circumflex'), ('uuml', '252', 'Latin small letter u with diaeresis'), ('yacute', '253', 'Latin small letter y with acute'), ('thorn', '254', 'Latin small letter thorn'), ('yuml', '255', 'Latin small letter y with diaeresis'), ('fnof', '402', 'Latin small f with hook'), ('Alpha', '913', 'Greek capital letter alpha'), ('Beta', '914', 'Greek capital letter beta'), ('Gamma', '915', 'Greek capital letter gamma'), ('Delta', '916', 'Greek capital letter delta'), ('Epsilon', '917', 'Greek capital letter epsilon'), ('Zeta', '918', 'Greek capital letter zeta'), ('Eta', '919', 'Greek capital letter eta'), ('Theta', '920', 'Greek capital letter theta'), ('Iota', '921', 'Greek capital letter iota'), ('Kappa', '922', 'Greek capital letter kappa'), ('Lambda', '923', 'Greek capital letter lambda'), ('Mu', '924', 'Greek capital letter mu'), ('Nu', '925', 'Greek capital letter nu'), ('Xi', '926', 'Greek capital letter xi'), ('Omicron', '927', 'Greek capital letter omicron'), ('Pi', '928', 'Greek capital letter pi'), ('Rho', '929', 'Greek capital letter rho'), ('Sigma', '931', 'Greek capital letter sigma'), ('Tau', '932', 'Greek capital letter tau'), ('Upsilon', '933', 'Greek capital letter upsilon'), ('Phi', '934', 'Greek capital letter phi'), ('Chi', '935', 'Greek capital letter chi'), ('Psi', '936', 'Greek capital letter psi'), ('Omega', '937', 'Greek capital letter omega'), ('alpha', '945', 'Greek small letter alpha'), ('beta', '946', 'Greek small letter beta'), ('gamma', '947', 'Greek small letter gamma'), ('delta', '948', 'Greek small letter delta'), ('epsilon', '949', 'Greek small letter epsilon'), ('zeta', '950', 'Greek small letter zeta'), ('eta', '951', 'Greek small letter eta'), ('theta', '952', 'Greek small letter theta'), ('iota', '953', 'Greek small letter iota'), ('kappa', '954', 'Greek small letter kappa'), ('lambda', '955', 'Greek small letter lambda'), ('mu', '956', 'Greek small letter mu'), ('nu', '957', 'Greek small letter nu'), ('xi', '958', 'Greek small letter xi'), ('omicron', '959', 'Greek small letter omicron'), ('pi', '960', 'Greek small letter pi'), ('rho', '961', 'Greek small letter rho'), ('sigmaf', '962', 'Greek small letter final sigma'), ('sigma', '963', 'Greek small letter sigma'), ('tau', '964', 'Greek small letter tau'), ('upsilon', '965', 'Greek small letter upsilon'), ('phi', '966', 'Greek small letter phi'), ('chi', '967', 'Greek small letter chi'), ('psi', '968', 'Greek small letter psi'), ('omega', '969', 'Greek small letter omega'), ('thetasym', '977', 'Greek small letter theta symbol'), ('upsih', '978', 'Greek upsilon with hook symbol'), ('piv', '982', 'pi symbol'), ('bull', '8226', 'bullet'), ('hellip', '8230', 'horizontal ellipsis'), ('prime', '8242', 'prime'), ('Prime', '8243', 'double prime'), ('oline', '8254', 'overline'), ('frasl', '8260', 'fraction slash'), ('weierp', '8472', 'script capital'), ('image', '8465', 'blackletter capital I'), ('real', '8476', 'blackletter capital R'), ('trade', '8482', 'trade mark sign'), ('alefsym', '8501', 'alef symbol'), ('larr', '8592', 'leftward arrow'), ('uarr', '8593', 'upward arrow'), ('rarr', '8594', 'rightward arrow'), ('darr', '8595', 'downward arrow'), ('harr', '8596', 'left right arrow'), ('crarr', '8629', 'downward arrow with corner leftward'), ('lArr', '8656', 'leftward double arrow'), ('uArr', '8657', 'upward double arrow'), ('rArr', '8658', 'rightward double arrow'), ('dArr', '8659', 'downward double arrow'), ('hArr', '8660', 'left-right double arrow'), ('forall', '8704', 'for all'), ('part', '8706', 'partial differential'), ('exist', '8707', 'there exists'), ('empty', '8709', 'empty set'), ('nabla', '8711', 'nabla'), ('isin', '8712', 'element of'), ('notin', '8713', 'not an element of'), ('ni', '8715', 'contains as member'), ('prod', '8719', 'n-ary product'), ('sum', '8721', 'n-ary summation'), ('minus', '8722', 'minus sign'), ('lowast', '8727', 'asterisk operator'), ('radic', '8730', 'square root'), ('prop', '8733', 'proportional to'), ('infin', '8734', 'infinity'), ('ang', '8736', 'angle'), ('and', '8743', 'logical and'), ('or', '8744', 'logical or'), ('cap', '8745', 'intersection'), ('cup', '8746', 'union'), ('int', '8747', 'integral'), ('there4', '8756', 'therefore'), ('sim', '8764', 'tilde operator'), ('cong', '8773', 'approximately equal to'), ('asymp', '8776', 'almost equal to'), ('ne', '8800', 'not equal to'), ('equiv', '8801', 'identical to'), ('le', '8804', 'less-than or equal to'), ('ge', '8805', 'greater-than or equal to'), ('sub', '8834', 'subset of'), ('sup', '8835', 'superset of'), ('nsub', '8836', 'not a subset of'), ('sube', '8838', 'subset of or equal to'), ('supe', '8839', 'superset of or equal to'), ('oplus', '8853', 'circled plus'), ('otimes', '8855', 'circled times'), ('perp', '8869', 'up tack'), ('sdot', '8901', 'dot operator'), ('lceil', '8968', 'left ceiling'), ('rceil', '8969', 'right ceiling'), ('lfloor', '8970', 'left floor'), ('rfloor', '8971', 'right floor'), ('lang', '9001', 'left-pointing angle bracket'), ('rang', '9002', 'right-pointing angle bracket'), ('loz', '9674', 'lozenge'), ('spades', '9824', 'black (solid) spade suit'), ('clubs', '9827', 'black (solid) club suit'), ('hearts', '9829', 'black (solid) heart suit'), ('diams', '9830', 'black (solid) diamond suit'), ('quot', '34', 'quotation mark'), ('amp', '38', 'ampersand'), ('lt', '60', 'less-than sign'), ('gt', '62', 'greater-than sign'), ('OElig', '338', 'Latin capital ligature OE'), ('oelig', '339', 'Latin small ligature oe'), ('Scaron', '352', 'Latin capital letter S with caron'), ('scaron', '353', 'Latin small letter s with caron'), ('Yuml', '376', 'Latin capital letter Y with diaeresis'), ('circ', '710', 'modifier letter circumflex accent'), ('tilde', '732', 'small tilde'), ('ensp', '8194', 'en space'), ('emsp', '8195', 'em space'), ('thinsp', '8201', 'thin space'), ('zwnj', '8204', ' zero width non-joiner'), ('zwj', '8205', 'zero width joiner'), ('lrm', '8206', 'left-to-right mark'), ('rlm', '8207', 'right-to-left mark'), ('ndash', '8211', 'en dash'), ('mdash', '8212', 'em dash'), ('lsquo', '8216', 'left single quotation mark'), ('rsquo', '8217', 'right single quotation mark'), ('sbquo', '8218', 'single low-9 quotation mark'), ('ldquo', '8220', 'left double quotation mark'), ('rdquo', '8221', 'right double quotation mark'), ('bdquo', '8222', 'double low-9 quotation mark'), ('dagger', '8224', 'dagger'), ('Dagger', '8225', 'double dagger'), ('permil', '8240', 'per mille sign'), ('lsaquo', '8249', 'single left-pointing angle quotation'), ('rsaquo', '8250', 'single right-pointing angle quotation'), ('euro', '8364', 'euro sign')]]

del makeEntity

from oaipmh.metadata import MetadataReader

oai_ddi_reader = MetadataReader(
    fields={
        'title':        ('textList', 'oai_ddi:codeBook/stdyDscr/citation/titlStmt/titl/text()'),  # noqa
        'creator':      ('textList', 'oai_ddi:codeBook/stdyDscr/citation/rspStmt/AuthEnty/text()'),  # noqa
        'subject':      ('textList', 'oai_ddi:codeBook/stdyDscr/stdyInfo/subject/keyword/text()'),  # noqa
        'description':  ('textList', 'oai_ddi:codeBook/stdyDscr/stdyInfo/abstract/text()'),  # noqa
        'publisher':    ('textList', 'oai_ddi:codeBook/stdyDscr/citation/distStmt/contact/text()'),  # noqa
        'contributor':  ('textList', 'oai_ddi:codeBook/stdyDscr/citation/contributor/text()'),  # noqa
        'date':         ('textList', 'oai_ddi:codeBook/stdyDscr/citation/prodStmt/prodDate/text()'),  # noqa
        'series':       ('textList', 'oai_ddi:codeBook/stdyDscr/citation/serStmt/serName/text()'),  # noqa
        'type':         ('textList', 'oai_ddi:codeBook/stdyDscr/stdyInfo/sumDscr/dataKind/text()'),  # noqa
        'format':       ('textList', 'oai_ddi:codeBook/fileDscr/fileType/text()'),  # noqa
        'identifier':   ('textList', "oai_ddi:codeBook/stdyDscr/citation/titlStmt/IDNo/text()"),  # noqa
        'source':       ('textList', 'oai_ddi:codeBook/stdyDscr/dataAccs/setAvail/accsPlac/@URI'),  # noqa
        'language':     ('textList', 'oai_ddi:codeBook/@xml:lang'),  # noqa
        'tempCoverage': ('textList', 'oai_ddi:codeBook/stdyDscr/stdyInfo/sumDscr/timePrd/text()'),  # noqa
        'geoCoverage':  ('textList', 'oai_ddi:codeBook/stdyDscr/stdyInfo/sumDscr/geogCover/text()'),  # noqa
        'rights':       ('textList', 'oai_ddi:codeBook/stdyInfo/citation/prodStmt/copyright/text()')   # noqa
    },
    namespaces={
        'oai_ddi': 'http://www.icpsr.umich.edu/DDI',
    }
)

# Note: maintainer_email is not part of Dublin Core
oai_dc_reader = MetadataReader(
    fields={
        'title':            ('textList', 'oai_dc:dc/dc:title/text()'),  # noqa
        'creator':          ('textList', 'oai_dc:dc/dc:creator/text()'),  # noqa
        'subject':          ('textList', 'oai_dc:dc/dc:subject/text()'),  # noqa
        'description':      ('textList', 'oai_dc:dc/dc:description/text()'),  # noqa
        'publisher':        ('textList', 'oai_dc:dc/dc:publisher/text()'),  # noqa
        'maintainer_email': ('textList', 'oai_dc:dc/oai:maintainer_email/text()'),  # noqa
        'contributor':      ('textList', 'oai_dc:dc/dc:contributor/text()'),  # noqa
        'date':             ('textList', 'oai_dc:dc/dc:date/text()'),  # noqa
        'type':             ('textList', 'oai_dc:dc/dc:type/text()'),  # noqa
        'format':           ('textList', 'oai_dc:dc/dc:format/text()'),  # noqa
        'identifier':       ('textList', 'oai_dc:dc/dc:identifier/text()'),  # noqa
        'source':           ('textList', 'oai_dc:dc/dc:source/text()'),  # noqa
        'language':         ('textList', 'oai_dc:dc/dc:language/text()'),  # noqa
        'relation':         ('textList', 'oai_dc:dc/dc:relation/text()'),  # noqa
        'coverage':         ('textList', 'oai_dc:dc/dc:coverage/text()'),  # noqa
        'rights':           ('textList', 'oai_dc:dc/dc:rights/text()')  # noqa
    },
    namespaces={
    'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    'oai': 'http://www.openarchives.org/OAI/2.0/',
    'dc': 'http://purl.org/dc/elements/1.1/'}
)

from oaipmh.metadata import MetadataReader

oai_ddi_reader = MetadataReader(
    fields={
        'title':       ('textList', 'oai_ddi:codeBook/oai_ddi:stdyDscr/citation/titlStmt/title/text()'),
        'creator':     ('textList', 'oai_ddi:codeBook/oai_ddi:stdyDscr/citation/rspStmt/AuthEnty/text()'),
        'subject':     ('textList', 'oai_dc:dc/dc:subject/text()'),
        'description': ('textList', 'oai_dc:dc/dc:description/text()'),
        'publisher':   ('textList', 'oai_dc:dc/dc:publisher/text()'),
        'contributor': ('textList', 'oai_dc:dc/dc:contributor/text()'),
        'date':        ('textList', 'oai_dc:dc/dc:date/text()'),
        'type':        ('textList', 'oai_dc:dc/dc:type/text()'),
        'format':      ('textList', 'oai_dc:dc/dc:format/text()'),
        'identifier':  ('textList', 'oai_dc:dc/dc:identifier/text()'),
        'source':      ('textList', 'oai_dc:dc/dc:source/text()'),
        'language':    ('textList', 'oai_dc:dc/dc:language/text()'),
        'relation':    ('textList', 'oai_dc:dc/dc:relation/text()'),
        'coverage':    ('textList', 'oai_dc:dc/dc:coverage/text()'),
        'rights':      ('textList', 'oai_dc:dc/dc:rights/text()')
    },
    namespaces={
        'oai_ddi': 'http://www.icpsr.umich.edu/DDI',
    }
)

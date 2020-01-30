from ansible.errors import AnsibleError


class FilterModule(object):

    def filters(self):
        return {
            'xml2json': self.xml2json,
            'xml2dict': self.xml2dict,
        }

    def xml2json(self, value):
        try:
            import xmltodict
            import json
            return json.dumps(xmltodict.parse(value))
        except Exception as e:
            raise AnsibleError(e)

    def xml2dict(self, value):
        try:
            import xmltodict
            return xmltodict.parse(value)
        except Exception as e:
            raise AnsibleError(e)

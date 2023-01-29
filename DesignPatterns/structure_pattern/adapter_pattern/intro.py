import xmltodict

class TransJsonToXML:
    def __init__(self):
        self.name = "trans_json_to_xml"

    def json_to_xml(self, json_type=None):
        return xmltodict.unparse(json_type)

class TransXmlToJson:
    def __init__(self):
        self.name = "trans_xml_to_json"

    def xml_to_json(self, xml_string=None):
        return xmltodict.parse(xml_string)

# 객체들의 인터페이스를 통합하는 어뎁터 클래스.
class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    # attr을 self에서 찾을 수 없을 때 호출되는 메서드.
    def __getattr__(self, attr):
        return getattr(self.obj, attr)


if __name__ == "__main__":
    # 간단한 예시로 xml 데이터와 json 데이터 생성
    json_type = {"data": {"name": "abc"}}
    xml_string = '<data><name>abc</name></data>'

    trans_xml = TransJsonToXML()
    trans_json = TransXmlToJson()

    objects = [
        Adapter(trans_xml, get_data=trans_xml.json_to_xml(json_type)),
        Adapter(trans_json, get_data=trans_json.xml_to_json(xml_string))
    ]

    for obj in objects:
        print(f"{obj.name}: {obj.get_data}")

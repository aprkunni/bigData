import xml.etree.ElementTree as ET

# XML 파일 불러오기
tree = ET.parse('test.xml')
root = tree.getroot()

# XML 구조 확인하기
print("Root Element:", root.tag)
print("Attributes of Root:", root.attrib)

# XML 내용 탐색
for child in root:
    print(f"Tag: {child.tag}, Attributes: {child.attrib}, Text: {child.text}")

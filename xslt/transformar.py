from lxml import etree
from pathlib import Path

base_path = Path(__file__).parent.parent
xml_file = base_path / "datos" / "datos.xml"
xslt_file = base_path / "xslt" / "plantilla.xslt"
output_file = base_path / "xslt" / "salida.html"

xml = etree.parse(str(xml_file))
xslt = etree.parse(str(xslt_file))
transform = etree.XSLT(xslt)
result = transform(xml)

with open(output_file, "wb") as f:
    f.write(etree.tostring(result, pretty_print=True))

print("Transformación XML -> HTML completada")
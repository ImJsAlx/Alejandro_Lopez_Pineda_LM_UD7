from pathlib import Path
import xmltodict
import json

base_path = Path(__file__).parent
xml_file = base_path / "datos.xml"
json_file = base_path / "datos.json"

with open(xml_file, "r", encoding="utf-8") as f:
    xml_data = f.read()

data_dict = xmltodict.parse(xml_data)

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data_dict, f, indent=4, ensure_ascii=False)

print("Conversión XML -> JSON completada")
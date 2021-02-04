import json
# Access the value of key2 from the following JSON
sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'])

print(" ")
sampleJson = {"key1": "value1", "key2": "value2"}
prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

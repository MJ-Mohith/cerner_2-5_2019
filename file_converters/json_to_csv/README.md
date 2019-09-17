# Converts JSON File to CSV File

## To Execute ::

```shell
python json2csv.py -i test.json -o test.csv 
```

### test.json

```json
[
    {
      "Developer": "Test1_Developer",
      "Tester": "Test1_Tester",
      "Ops": "Test1_OPS"
    },
    {
        "Developer": "Test2_Developer",
        "Tester": "Test2_Tester",
        "Ops": "Test2_OPS"
      }, 
      {
        "Developer": "Test3_Developer",
        "Tester": "Test3_Tester",
        "Ops": "Test3_OPS"
      }, 
      {
        "Developer": "Test4_Developer",
        "Tester": "Test4_Tester",
        "Ops": "Test4_OPS"
      }, 
      {
        "Developer": "Test5_Developer",
        "Tester": "Test5_Tester",
        "Ops": "Test5_OPS"
      }
  ]
```

### test.csv

```txt
Ops,Tester,Developer
Test1_OPS,Test1_Tester,Test1_Developer
Test2_OPS,Test2_Tester,Test2_Developer
Test3_OPS,Test3_Tester,Test3_Developer
Test4_OPS,Test4_Tester,Test4_Developer
Test5_OPS,Test5_Tester,Test5_Developer
```

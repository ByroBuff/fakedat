# fakedat
## Installation
```
git clone https://github.com/ByroBuff/fakedat
cd fakedat
python main.py -i input.json -o output.txt
```

## template example
```json
{
    "_iter_variables": {
        "firstName": "|first_name()",
        "lastName": "|last_name()"
    },
    "_repeat": 1000,
    "template": {
        "uuid": "|uuid()",
        "name": "{firstName} {lastName}",
        "username": "|username()",
        "age": "|number('18', '100')",
        "email": "|email({firstName}, {lastName})",
        "phone": "|phone()",
        "ssn": "|ssn()",
        "birthday": "|date('%B %d, %Y', '1950-01-01', '2000-01-01')"
    }
}
```

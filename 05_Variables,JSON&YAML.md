# Variables

## bash

- you can store variables on terminal sessions
- these variables are deleted when the sessions closes
- this is important for bash scripting
- in bash you need to use $ to call a variable

### example bash

- skill="devOps"
- echo $skill
  - devOps
- echo skill
  - skill
- echo "I am learning $skill"
  - I am learning devOps
    _if you use single quotes it wont work_
- echo 'I am learning $skill'
  - I am learning $skill

## python

- pretty basic
- you can find an online pything compiler or just use vscode, but there is a little extra work to do it on vscode, google a tutorial or something, IDK, Im not your mother, do some work on your own
- I just did this as a python file in [samples/05/variables.py](samples/05/variables.py)

# JSON & YAML (yet another markup language)

- These are how you save large data.
- JSON is used for data storage
- YAML is mostly used for configs in devops because its a little nicer to read
- I made the examples in the [samples/05/json.json](samples/05/json.json) and [samples/05/yaml.yaml](samples/05/yaml.yaml)

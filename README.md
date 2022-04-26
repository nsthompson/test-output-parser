# test-output-parser

This is a utility to generate both Rich CLI and Markdown formatted output for the following test frameworks:

* Robot Framework

## Installation

```shell
pip install -r requirements.txt
```

## Usage

### Help

```shell
python3 parser.py --help
```

### Output

```shell
 Usage: parser.py [OPTIONS]                                                                                                                                                         
                                                                                                                                                                                    
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  *  --framework    [robot]         Test Framework: [robot] for Robot framework [required]                                                                                        │
│  *  --file         PATH            Path to test output file [required]                                                                                                           │
│  *  --output       [cli|markdown]  Output Method: [cli] for rich command-line output [markdown] for markdown formatted tables [required]                                         │
│     --help                         Show this message and exit.                                                                                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Framework Examples

### Robot Framework - CLI Output

```shell
python3 parser.py --framework robot --file <path-to-output.xml> --output cli
```

### Robot Framework - Markdown Output

```shell
python3 parser.py --framework robot --file <path-to-output.xml> --output markdown
```

## Contributors

* Nick Thompson <@nsthompson>

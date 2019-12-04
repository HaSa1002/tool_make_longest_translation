# Python Tool: Make Longest Translation #
A simple CSV entry length checker, useful to test UIs with longest translation.
## Compatability ##
| Version | Compatible |
| ------- |:----------:|
| **3.8** | yes        |
| **<3.8**| untested   |

If you used it on a earlier version, please go ahead and open an issue.

## Usage ##


```
py make_longest_translation.py -h
```
Displays the help message

```
py make_longest_translation.py FILE
py make_longest_translation.py FILE [-out OUTFILE] [-delim DELIM] [-code CODE]
```
```
	FILE: 		The Source CSV Translation File
	OUTFILE: 	The Output CSV Translation File. Content will be overwritten. If omitted, the output will be written into the source file
	DELIM:		The delimeteting character. Default: ;
	CODE:		The language code in which the longest entries are saved. Default: aa (Afar)
```

Licensed as Public Domain
# pyls

Simple version of ls program for process illustration.

The `pyls` program  lists the entries in a directory with the output format
controlled through a small set of command line flags.

As is common, you can use the `-h` or `--help` flags to show help text
on how to use the program.

## Example usage

Without any arguments, it lists the contents of the current directory.
```
>  pyls
file1.txt
file2.pdf
dir3
dir4
```

`-F` adds a descriptive character to the of the file name that shows what
type it is.

```
>  pyls -F
file1.txt
file2.pdf
dir3/
dir4/
script10*
file109.py
```

The `-l` flag gives more information about files such as last modified time and
the file size. It can be clubbed with the `-F` flag as well.

```
> pyls -l
2024-04-12 16:04:23   2454  file1.txt
2023-05-25 07:37:56   1712  file2.txt
2024-06-20 01:23:12      0  dir3
2022-05-19 15:31:43      0  dir4
2023-04-16 19:51:45   4876  script10
2024-06-30 21:07:22  93487  file109.py
```



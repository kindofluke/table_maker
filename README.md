# TableMaker

Simple script that takes the first line of a datafile and prints it to STD_OUT and copies it to the system clipboard. 

Usage 

```
>: python table_maker.py test.csv
hello
goodby
column
1
```

Optional you can use delimiter

```
>: python table_maker.py -d ',' test.csv
hello
goodby
column
1
```

Create an alias  in your bashprofile

```
alias tablem="python [PATH TO PROJECT]/table_maker.py"
```



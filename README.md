# CharReplace
CharReplace: a multipurpose program to replace special characters in file/directories names or rename files/directories

## Help

python3 CharReplace.py -h

## Usage

`python3 CharReplace.py <directory/input_dir> <Char_to_replace, 1= one, 2= many> <what_to_replace> <what_to_replace_with>")`

* positional arguments
  - position 1 = input directory
  - position 2 = number of characters to replace, 1 = one character, 2 = multiple characters
  - position 3 = characters to replace (white space must be with quotes)
  - position 4 = new characer introduced, (white space must be with quotes)

### Example

#### replace spaces with underscore

`python3 CharReplace.py <input_dir> 1 ' ' '_'`

#### replae multiple characters with underscore

`python3 CharReplace.py <input_dir> 2 '.)[(])/ ' '_' `

#### change file extensions

`python3 CharReplace.py <input_dir> 1 '.csv' '.txt'`

#### removing complex special characer structures for example ._ or __ (double underscore)

`python3 CharReplace.py <input_dir> 1 '._' '_'`

`python3 CharReplace.py <input_dir> 1 '__' '_'`

# CharReplace
CharReplace: a multipurpose program to replace special characters in file/directories names or rename files/directories

## Help

python3 CharReplace.py -h

## Usage

`python3 CharReplace.py <directory/input_dir> <Char_to_replace, 1= one, 2= many> <what_to_replace> <what_to_replace_with>")`

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

# CharReplace
Replace special characters from file or directory names


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

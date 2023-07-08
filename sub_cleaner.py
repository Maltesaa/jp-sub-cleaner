import os
import re

# Set the directory path containing the SRT files to convert
dir_path = os.getcwd()

def hankaku_to_zenkaku_katakana(string):
    hankaku_katakana = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝﾞﾟ"
    zenkaku_katakana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンヴ"

    mapping = str.maketrans(dict(zip(hankaku_katakana, zenkaku_katakana)))
    return string.translate(mapping)

try:
    # Loop through all files in the directory with .srt extension
    for filename in os.listdir(dir_path):
        if filename.endswith('.srt'):
            # Read the contents of the SRT file
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Process each line
            modified_lines = []
            for line in lines:
                if not re.match(r'^\d\d\:\d\d\:', line):
                    # Convert half-width katakana characters to full-width katakana characters
                    line = hankaku_to_zenkaku_katakana(line)

                    # Remove annoying characters
                    list_to_remove = ["♪♪～", ":", "♬～", " : ", "》", "《", "My Styles :)"]
                    for c in list_to_remove:
                        line = line.replace(c, "")

                    # Remove lines that only include sound effects
                    pattern = r'^(\(|\（)([ぁ-んァ-ン一-龯\w])*(\)|\）)$'
                    line = re.sub(pattern, "", line)

                modified_lines.append(line)

            # Write the modified lines back to the same file
            with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
                f.writelines(modified_lines)
                print("Converted " + filename)
except Exception as e:
    print("Something went wrong: ", e)

input("\nPress enter to exit...")

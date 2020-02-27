import os

path = './'
total_len = 0; 
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk('./'):
    for file in f:
        if '.md' in file:
            cur_path = os.path.join(r, file); 
            with open(cur_path, 'r') as content_file:
                content = content_file.read()
                wordCount = content.split()
                total_len += len(wordCount)
                # print (r + ': %s', wordCount)
                content = None
                wordCount = None

print("Total word ", total_len); 

#!/bin/python3

def write_output_to_file(file_name, input):
    file = open("/path/to/folder/"+file_name, 'w')
    file.write(str(input))

following = []

followers = []

    
already_unf = []
whitelist = []
res = [c for c in following if c not in followers and c not in whitelist and c not in already_unf]
print("<-------------->\n\nNot following back:\n",res)
print("\n<-------------->\n\nNot following back:",len(res),"\nFollowing:",len(following),"\nFollowers:",len(followers))

write_output_to_file("output.txt",res)

followers_old = []

old = [c for c in followers_old if c not in followers]
new = [c for c in followers if c not in followers_old and len(c) > 1]
print("\n<-------------->\n\nNot following you yet:",old)
print("\n<-------------->\n\nStarted following you since last time:",new,"\n<-------------->")


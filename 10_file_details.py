import os
path="1_datatypes.py"
fd=os.open(path,os.O_RDWR)
info=os.fstat(fd)

print(f"Device containing file:{info.st_nlink}")
print(f"Inode numner:{info.st_ino}")
print(f"Protection:{info.st_mode}")
print(f"Number of hardlink:{info.st_nlink}")
print(f"User ID:{info.st_uid}")
print(f"Group ID:{info.st_gid}")
print(f"Size of file in Bytes:{info.st_size}")
print(f"Last modiification time:{info.st_mtime}")
print(f"Last access time:{info.st_atime}")
print(f"Last status chage:{info.st_ctime}")


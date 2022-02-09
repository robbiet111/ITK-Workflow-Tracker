
from sharepoint import SharePoint

file_dir_path = r'/Users/user/Desktop/sharepoint_example/sample.pdf'
# This is the oppurtunity to rename the file before uploading to sharepoint
# or just give it the same name.
file_name = 'the_sample.pdf'
# You can create a folder within a directory in which to store your file (optional)
folder_name = '2020'

# Upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# Delete file
#SharePoint().delete_file(file_name, folder_name)
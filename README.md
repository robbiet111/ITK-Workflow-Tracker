# ITk workflow tracker

## Contributors
- [Robbie Tippen](https://stgit.dcs.gla.ac.uk/2403237t), 2403237T
- [Jakub Jelinek](https://stgit.dcs.gla.ac.uk/2478625j), 2478625J

## Main customer
- Dima Maneuski

## Project itself
- Using python API (Shareplum) to connect to microsoft sharepoint.
- Implementing Power Automate functionality over microsoft sharepoint.

## How to use Shareplum to upload or delete files to Sharepoint

1.	In the 'config.json' file swap the username and password with that of the one you will use for your Sharepoint. 
![p1](uploads/17ba0209317c8e519473cea3663f164c/p1.png)

2.	Change the url variable to match the general Sharepoint url and the site variable to match that of the specific site within that Sharepoint you want to access. 

3.	'doc_library' is set to "Shared Documents" which is basically the main directory, if you have sub-folders within that you can add them on like "Shared Documents/[insert name of sub-folder]".

4.	In project.py replace what is in the quotation marks for ‘file_dir_path’ with the local directory path to the file you want to upload.
![p4](uploads/5dd33a01e3be9be403bb546108cc31ec/p4.png)

5.	If you want to upload a file then uncomment the line of code under '# Upload file' (make sure the line of code under '# Delete file' is commented out)
![p5](uploads/a9e827f20e04a2b99d433656910e4aab/p5.png)

6.	If you want to delete a file then uncomment the line of code under '# Delete file' (make sure the line of code under '# Upload file' is commented out)
![p6](uploads/2c5db90cc833dabf58e399492385dee1/p6.png)

7.	Finally run the ‘project.py’ file and the entered file will appear in Sharepoint

## How to run example_test
In the 'config.json' file swap the username and password with that of the one you will use for your Sharepoint. Change the url variable to match the general Sharepoint url and the site variable to match that of the specific site within that Sharepoint you want to access. 'doc_library' is set to "Shared Documents" which is basically the main directory, if you have sub-folders within that you can add them on like "Shared Documents/[insert name of sub-folder]".

In project.py you would just replace whats in the quotation marks with the directory path to the file you want to upload and then if you want to upload a file then uncomment the line of code under '# Upload file' and it's the same process with 'Delete file'.

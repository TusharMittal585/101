import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        print(" dropbox account linked")
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root.fileName) 
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)     

                with open(local_path,'rb') as f: 
                    dbx.files_upload(f.read(),dropbox_path, mode=dropbox.files.WriteMode.overwrite) 
       

        
        

def main():
    access_token = 'sl.BJcPRCknLA811eBg0KRo4uM8RecpOrUbgR-RkRlw-F1MTzWr6XjMdlDKkIKzXzJTKAxNQaT12vnb78Og-_HV72uTeIIY9pAXrfUYHHGPKk0MbqxQuxTlu4_gVLw75oPmHMn2CN3fOO9s'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer : -") 
    file_to = input("enter the full path to upload to dropbox:- ") 
    transferData.upload_file(file_from, file_to)
    print('Files have been moved')


main()


 
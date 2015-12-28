#! python3
# backup-to-zip.py
# Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def createZipFilename(folder):
    """
    Figures out which filename should be used based on what files already exist.
    """
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    return zip_filename

def backupToZip(folder):
    """
    Backs up the entire content of a folder into a zip file.
    """
    folder = os.path.abspath(folder)

    zip_filename = createZipFilename(folder)

    print("Creating %s..." % zip_filename)
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s" % foldername)
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print("Done.")

backupToZip("/Users/mac/Documents")

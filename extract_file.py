import zipfile as zp 
with zp.ZipFile('D:/edufly/cricketer_cnn/archive (7).zip', 'r') as zip_ref:
    zip_ref.extractall('cricketer_cnn')
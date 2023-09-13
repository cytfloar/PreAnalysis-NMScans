import os, csv
import pandas as pd
folder_list= pd.read_csv("conversion_list.csv")

def convert(sub, ses):
  os.system(f"""/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f "sub-{sub}_ses-{ses}_STRUC_2D_GRE_MT_1p5mm_NEX5_18" -p y -z y -o "horga/{sub}/NM_NEX5" "NM Pilot Phase 2/{ses}/scans/3-STRUC_2D_GRE_MT_1p5mm_NEX5/resources/DICOM/files" """)
  os.system(f"""/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f "sub-{sub}_ses-{ses}_T1w" -p y -z y -o "horga/{sub}/T1w" "NM Pilot Phase 2/{ses}/scans/2-STRUC_T1MPRAGE_noPROMO/resources/DICOM/files" """)

for i, row in folder_list.iterrows():
  sub = row['sub']
  ses = row['ses']
  convert(sub, ses)
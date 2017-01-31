# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:11:58 2017

@author: Sammed Mandape

This code is to parse clinical features of publicly available cancer dataset
from GDC portal for TCGA project.

"""

import os
import xml.etree.ElementTree as ET

# Uncomment the following for AA patients
#os.chdir("E:/Gladus/Pancreatic Cancer/African American/Clinical")

# The following is for white patients
os.chdir("E:\Gladus\Pancreatic Cancer\White\Clinical")


top = os.getcwd()

f = open ("final_output_1.txt", "a")
f.writelines("patid \t bcr_patient_barcode \t tumor_tissue_site \t histological_type \t tumor_type \t anatomic_neoplasm_subdivision \t gender \t days_to_birth \t race \t ethnicity \tage_at_initial_pathologic_diagnosis \t clinical_stage \t pathologic_stage \t gleason_score \t vital_status \t days_to_last_followup \t days_to_death \t patient_death_reason \t history_of_chronic_pancreatitis \t family_history_of_cancer \n")


for root, dirs, files in os.walk(top):
    for name in files:
        if name.endswith((".xml")):
            # Test if files are read and print the name of those files.
            #print (name)

            tree = ET.parse(str.join('\\',(root, name)))
            root = tree.getroot()

            for patient in root.iter('{http://tcga.nci/bcr/xml/shared/2.7}patient_id'):
                print (patient.text)
    
            for patient in root.iter('{http://tcga.nci/bcr/xml/clinical/paad/2.7}patient'):
                patid = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}patient_id').text
                bcr_patient_barcode = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}bcr_patient_barcode').text
                tumor_tissue_site = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}tumor_tissue_site').text
                histological_type = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}histological_type').text
                tumor_type = patient.find('{http://tcga.nci/bcr/xml/clinical/paad/2.7}tumor_type').text
                anatomic_neoplasm_subdivision = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}anatomic_neoplasm_subdivision').text
                gender = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}gender').text
                days_to_birth = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}days_to_birth').text
                race = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}race_list').find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}race').text
                ethnicity = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}ethnicity').text
                age_at_initial_pathologic_diagnosis = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}age_at_initial_pathologic_diagnosis').text
                clinical_stage = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}stage_event').find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}clinical_stage').text
                pathologic_stage = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}stage_event').find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}pathologic_stage').text
                gleason_score = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}stage_event').find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}gleason_grading').find('{http://tcga.nci/bcr/xml/clinical/shared/stage/2.7}gleason_score').text
                vital_status = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}vital_status').text
                days_to_last_followup = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}days_to_last_followup').text
                days_to_death = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}days_to_death').text
                patient_death_reason = patient.find('{http://tcga.nci/bcr/xml/clinical/shared/2.7}patient_death_reason').text
                history_of_chronic_pancreatitis = patient.find ('{http://tcga.nci/bcr/xml/clinical/paad/2.7}history_of_chronic_pancreatitis').text
                family_history_of_cancer = patient.find ('{http://tcga.nci/bcr/xml/clinical/paad/2.7}family_history_of_cancer').text
                f.write("%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\n" % (patid, bcr_patient_barcode, tumor_tissue_site, histological_type, tumor_type, anatomic_neoplasm_subdivision, gender, days_to_birth, race, ethnicity,  age_at_initial_pathologic_diagnosis, clinical_stage, pathologic_stage , gleason_score , vital_status , days_to_last_followup , days_to_death , patient_death_reason , history_of_chronic_pancreatitis , family_history_of_cancer))
                
                # Print to the console for testing
                """
                print(bcr_patient_barcode, '\n', 
                      tumor_tissue_site, '\n',
                      histological_type, '\n',
                      tumor_type, '\n',
                      anatomic_neoplasm_subdivision, '\n',
                      gender, '\n',
                      days_to_birth, '\n',
                      race, '\n',
                      ethnicity, '\n',
                      age_at_initial_pathologic_diagnosis, '\n',
                      clinical_stage, '\n',
                      pathologic_stage, '\n',
                      gleason_score, '\n',
                      vital_status, '\n',
                      days_to_last_followup, '\n',
                      days_to_death, '\n',
                      patient_death_reason, '\n',
                      history_of_chronic_pancreatitis, '\n',
                      family_history_of_cancer, '\n'
                      )
                """
f.close()
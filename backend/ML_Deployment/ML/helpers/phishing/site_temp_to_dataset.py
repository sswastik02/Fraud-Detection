import os,sys,io

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)
# Adding access to super parent directory

from paths import TEMP_DIR

def temp_files_to_dataset():
        legitimate_folder = os.path.join(TEMP_DIR,"legitimate")
        phishing_folder = os.path.join(TEMP_DIR,"phishing")

        if(not os.path.exists(legitimate_folder) or not os.path.exists(phishing_folder)):
            print("\nFolders needed to be created : ")
            print(os.path.join(TEMP_DIR,"legitimate"))
            print(os.path.join(TEMP_DIR,"phishing"))
            exit(0)
        
        files = []
        labels = []

        for _,_,f in os.walk(legitimate_folder):
            files.extend([os.path.join(legitimate_folder,file) for file in f])
            labels.extend([0 for _ in f])
        for _,_,f in os.walk(phishing_folder):
            files.extend([os.path.join(phishing_folder, file) for file in f])
            labels.extend([1 for _ in f])


        dataset_file_path = os.path.join(TEMP_DIR,"htmlCodePerLine.txt")
        dataset_file = open(dataset_file_path,"w")

        dataset = []
        count = 0
        for file in files:
            count = count + 1
            print("Files processed: %d, Total files: %d" % (count, len(files)))
            fileData = io.open(file, "r", errors="ignore").readlines()
            fileData = ''.join(str(line) for line in fileData)
            fileData = fileData.replace("\n", " ")
            dataset.extend([fileData + '\n'])
            dataset_file.write(fileData + "\n")
        dataset_file.close()

        return ((dataset,labels),dataset_file_path)
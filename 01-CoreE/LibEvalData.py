"""
    Data Auditing & Keyword Frequency Analysis Library
"""
import re

resultat = {}

def loadDataset(file, dico):
    """Loads a keyword file and initializes a counting dictionary.

    Args:
        file (str): Path to the keyword/expression file.
        dico (dict): The dictionary to be populated.
    """
    with open(file, 'r') as file:
        for line in file:
            resultat[line.split("\n")[0]] = 0

def recordic(file, dico):
    """Parses a dataset and counts occurrences of defined keywords or expressions.

    Args:
        file (file): Path to the dataset.
        dico (dict): Dictionary containing the keywords to track.
    """
    dico["LINE"] = 0
    dico["OCCUR"] = 0
    with open(file, 'r') as file:
        for e in file:
            dico["LINE"] += 1
            for k in dico.keys():
                if len(k.split(" ")) == 1:
                    for word in e.split(" "):
                        word = re.sub('[^a-z0-9àâäéèëêïîôöùûüÿç]+', '', word.lower())
                        if k == word:
                            dico[k] +=1
                            dico["OCCUR"]  +=1
                else:
                    if(k in e):
                        dico[k] +=1
                        dico["OCCUR"] +=1

def rapportR(dico, out):
    """Generates a statistical report on the dataset based on keyword density.

    Args:
        dico (dict): Keyword dictionary.
        out (str): Path to the output report file (.txt).
    """
    with open(out, 'a') as file:
        for k in dico.keys():
            if(k != "LINE"):
                file.write(f"{k}:{dico[k]}/{round(dico[k]/dico['LINE']*100, 4)}%\n")
        file.write(f"Total occurences:{dico['OCCUR']}/{round(dico['OCCUR']/dico['LINE']*100, 4)}%\n")

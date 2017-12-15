import os
import mysql.connector



def getUsableTableName(tableName):
    UsableTableName = tableName
    UsableTableName = UsableTableName.replace("'",'')
    UsableTableName = UsableTableName.replace("(",'')
    UsableTableName = UsableTableName.replace(")",'')
    UsableTableName = UsableTableName.replace(",",'')
    UsableTableName = UsableTableName[1:]
    UsableTableName = UsableTableName[0].upper()+UsableTableName[1:]
    return UsableTableName
def getUsableTableNameMin(tableName):
    UsableTableName = tableName
    UsableTableName = UsableTableName.replace("'",'')
    UsableTableName = UsableTableName.replace("(",'')
    UsableTableName = UsableTableName.replace(")",'')
    UsableTableName = UsableTableName.replace(",",'')
    UsableTableName = UsableTableName[1:]
    return UsableTableName











nameDB = raw_input("Nom de la base ?")
host = raw_input('Ip de la base ?')
user = raw_input('Nom d\'utilisateur ?')
password = raw_input('Mot de passe ?')
conn = mysql.connector.connect(host=host,user=user,password=password, database=nameDB)
cursor = conn.cursor()
cursor.execute("""SHOW TABLES""")
tables = cursor.fetchall()
conn.close()


try:
    os.mkdir('Controllers')
except OSError:
    pass
try:
    os.mkdir('Models')
except OSError:
    pass
try:
    os.mkdir('Views')
except OSError:
    pass
try:
    os.mkdir('Views/_Helpers')
except OSError:
    pass
i=0
numberTable = len(tables)
while(i<numberTable):


    ##CREATION DES FICHIERS DU CONTROLLER
    nomFichier = getUsableTableName(str(tables[i]))+'.php'
    try:
        fichier = open('Controllers/'+nomFichier, "w")
        fichier.write('<?php\nnamespace Controllers;\nuse Kernel\Session,\n    Kernel\Utils,\n    Kernel\View;\nclass '+getUsableTableName(str(tables[i]))+' extends \Kernel\Controller { \n    public static function _setAction($actionName){ \n        switch($actionName){ \n            case"display":\n                self::display();\n                break;\n            }\n        }\n    public static function display(){\n        $table'+getUsableTableName(str(tables[i]))+' = \Models\\'+getUsableTableName(str(tables[i]))+'::getAll();\n        self::setView(new View("'+getUsableTableName(str(tables[i]))+'","display"));\n        self::getView()->'+getUsableTableNameMin(str(tables[i]))+' = $table'+getUsableTableName(str(tables[i]))+';\n        }\n    }')
    except OSError:
        pass

    ##CREATION DES FICHIERS DU MODELS



    try:
        fichier = open('Models/'+nomFichier, "w")

        fichier.write("<?php\nnamespace Models;\nclass "+getUsableTableName(str(tables[i]))+" extends \Kernel\Object{\n    protected static $_table='"+getUsableTableNameMin(str(tables[i]))+"';\n}")
    except OSError:
        pass
    ##CREATION DES DOSSIER/FICHIERSDES VUES


    try:
        os.mkdir('Views/'+getUsableTableName(str(tables[i])))
    except OSError:
        pass
    try:
        fichier = open('Views/'+getUsableTableName(str(tables[i]))+'/display.php', "w")
        fichier.write("<?php \n")
        fichier.write("var_dump($this->$table"+getUsableTableName(str(tables[i]))+");")
    except OSError:
        pass
    try:
        fichier = open('Views/_Helpers/header.php', "w")
        fichier.write('<?php')
        fichier = open('Views/_Helpers/footer.php', "w")
        fichier.write('<?php')
    except OSError:
        pass
    i=i+1

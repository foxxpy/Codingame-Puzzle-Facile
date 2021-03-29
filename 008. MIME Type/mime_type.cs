using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()); // Number of elements which make up the association table.
        int Q = int.Parse(Console.ReadLine()); // Number Q of file names to be analyzed.
        int index = 0;
        string[,] EXTMT = new string[N, 2];
        string extension = "";
        string[] affichageFinal = new string[Q];

        for (int i = 0; i < N; i++)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            EXTMT[i, 0] = inputs[0]; // file extension
            EXTMT[i, 0] = EXTMT[i, 0].ToLower();
            EXTMT[i, 1] = inputs[1]; // MIME type.

        }

        for (int i = 0; i < Q; i++)
        {
            string FNAME = Console.ReadLine(); // One file name per line.
            extension = rechercherExtension(FNAME);
            index = verifierPresenceExtension(extension, EXTMT, affichageFinal, index, N);
        }

        affichageResultat(affichageFinal);
    }

    //On recherche l'extension dans le nom du fichier
    public static string rechercherExtension(string fichier)
    {
        int i = fichier.Length - 1;
        bool pointTrouve = false;
        string extension = "";

        //On cherche où se situe le point en partant de la fin
        do
        {
            if (fichier[i] == '.' && i < fichier.Length - 1)
            {
                pointTrouve = true;
                break;
            }
            i--;
        } while (i >= 0);

        if (pointTrouve)
        {
            i++;

            do
            {
                extension += fichier[i];
                i++;
            } while (i < fichier.Length);

            extension = extension.ToLower();

        }

        else extension = "UNKNOWN";



        return extension;
    }

    //On regarde si l'extension est présente dans le tableau MIME
    public static int verifierPresenceExtension(string extension, string[,] MIME, string[] affichageFinal, int index, int tailleMIME)
    {
        int i = 0;
        bool extensionTrouvee = false;
        do
        {
            if (extension == MIME[i, 0])
            {
                affichageFinal[index] = MIME[i, 1];
                extensionTrouvee = true;
                index++;
                break;
            }
            i++;
        } while (i < tailleMIME);

        if (extensionTrouvee == false)
        {
            affichageFinal[index] = "UNKNOWN";
            index++;
        }

        return index;
    }

    //On affiche le résultat 
    public static void affichageResultat(string[] affichageFinal)
    {
        for (int i = 0; i < affichageFinal.Length; i++)
        {
            Console.WriteLine(affichageFinal[i]);
        }
    }
}

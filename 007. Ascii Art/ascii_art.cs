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
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string chaine = "";
        string impression = "";
        string T = Console.ReadLine();

        //On parcourt la chaîne de caractères
        //Les lettres minuscules sont transformées en lettre majuscule
        //Les caractères erronés sont transformés en "?"
        for (int j = 0; j < T.Length; j++)
        {
            if (Convert.ToChar(T.Substring(j, 1)) >= 97 && Convert.ToChar(T.Substring(j, 1)) <= 122)
            {
                chaine += T.Substring(j, 1).ToUpper();
            }

            else if (Convert.ToChar(T.Substring(j, 1)) >= 65 && Convert.ToChar(T.Substring(j, 1)) <= 90)
            {
                chaine += T.Substring(j, 1);
            }

            else chaine += "?";

        }

        //Console.WriteLine(chaine);
        //Console.WriteLine(T);

        for (int i = 0; i < H; i++)
        {
            string ROW = Console.ReadLine();
            impression = "";

            for (int j = 0; j < chaine.Length; j++)
            {
                if (Convert.ToChar(chaine.Substring(j, 1)) >= 65 && Convert.ToChar(chaine.Substring(j, 1)) <= 90)
                {
                    impression += ROW.Substring((int)(Convert.ToChar(chaine.Substring(j, 1)) - 65) * L, L);
                }

                else
                {
                    impression += ROW.Substring(26 * L, L);
                }
            }
            Console.WriteLine(impression);
        }

    }
}
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
        string MESSAGE = Console.ReadLine();
        string byteArray = ConvertToBinary(MESSAGE);
        byteArray = suppressBitByte(byteArray);
        string messageUnaire = ConvertToUnary(byteArray);



        Console.WriteLine(messageUnaire);
    }

    //Permet de convertir un message en binaire
    public static string ConvertToBinary(string MESSAGE)
    {
        StringBuilder sb = new StringBuilder();

        foreach (char c in MESSAGE.ToCharArray())
        {
            sb.Append(Convert.ToString(c, 2).PadLeft(8, '0'));
        }

        return sb.ToString();
    }

    public static string suppressBitByte(string byteArray)
    {
        int i = 0;
        int j = 0;
        int suppress = 0;

        for (int k = 1; k < byteArray.Length; k++)
        {
            if (k % 8 == 0) suppress++;
        }

        char[] correctedByteArray = new char[byteArray.Length - suppress];


        while (i < byteArray.Length)
        {
            if (i % 8 != 0)
            {
                correctedByteArray[j] = byteArray[i];
                j++;
            }
            i++;
        }
        string returnByteArray = new string(correctedByteArray);
        return returnByteArray;
    }

    //Permet de convertir une chaine de caractère binaire en unaire
    public static string ConvertToUnary(string byteArray)
    {
        int i = 0;
        int j = 1;
        string messageUnaire = "";
        while (i < byteArray.Length - 1)
        {
            int recul = 0;
            if (byteArray[i] == '0')
            {
                messageUnaire += "00 ";
            }

            else if (byteArray[i] == '1')
            {
                messageUnaire += "0 ";
            }

            //On regarde combien de fois un bit similaire se répète
            while (i + j < byteArray.Length && byteArray[i + j] == byteArray[i])
            {
                j++;
            }

            for (int k = 0; k < j; k++)
            {
                if (k < (j - 1) || i + j >= byteArray.Length - 1) messageUnaire += "0";
                else messageUnaire += "0 ";
            }

            i += j;
            j = 1;
        }


        return messageUnaire;

    }
}
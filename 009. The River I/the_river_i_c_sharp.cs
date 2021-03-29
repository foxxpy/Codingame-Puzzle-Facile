using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Solution
{
    static void Main(string[] args)
    {
        long r1 = long.Parse(Console.ReadLine());
        long r2 = long.Parse(Console.ReadLine());

        //Tant que r1 et r2 ne sont pas égaux, on continue les suites
        while (r1 != r2)
        {

            if (r1 < r2)
            {
                r1 = river(r1);
            }

            else
            {
                r2 = river(r2);
            }
        }
        //Affichage du résultat
        Console.WriteLine(r1);
    }

    ///<summary>
    /// Renvoie le chiffre suivant de la suite donnée en paramètre
    ///<param name="r">Element de la suite</param>
    ///</summary>
    public static long river(long r)
    {
        string r_str = r.ToString();
        long total = 0;
        foreach (char c in r_str)
        {
            total += (long)char.GetNumericValue(c);
        }
        r += total;
        return r;
    }
}
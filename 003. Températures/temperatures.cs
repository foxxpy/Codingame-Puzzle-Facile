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
        string temperatureTemporaire = "";
        int temperatureTemporaireInt;
        int tempMin = -5527;
        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string temps = Console.ReadLine(); // the n temperatures expressed as integers ranging from -273 to 5526

        if (n == 1) tempMin = int.Parse(temps);

        else if (n != 0)
        {
            for (int i = 0; i < temps.Length; i++)
            {
                if (temps.Substring(i, 1) == " ")
                {
                    temperatureTemporaireInt = int.Parse(temperatureTemporaire);
                    temperatureTemporaire = "";
                    if (tempMin == null) tempMin = temperatureTemporaireInt;
                    else
                    {
                        if (tempMin < 0 && temperatureTemporaireInt > tempMin && temperatureTemporaireInt <= tempMin * (-1))
                        {
                            tempMin = temperatureTemporaireInt;
                        }

                        else if (tempMin > 0 && temperatureTemporaireInt < tempMin && temperatureTemporaireInt > (tempMin * (-1)))
                        {
                            tempMin = temperatureTemporaireInt;
                        }

                    }

                }

                else
                {
                    temperatureTemporaire += temps.Substring(i, 1);
                }

            } //Fin de la boucle For
        } //Fin du if(n != 0)

        else tempMin = 0;


        Console.WriteLine(tempMin);
    }
}
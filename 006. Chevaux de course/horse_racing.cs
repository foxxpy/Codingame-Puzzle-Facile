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
        int N = int.Parse(Console.ReadLine());
        int[] tab = new int[N];
        int answer = 2000000;
        int number;
        int temp;
        for (int i = 0; i < N; i++)
        {
            tab[i] = int.Parse(Console.ReadLine());

        }
        Array.Sort(tab);
        answer = rechercheIntervalleLePlusCourt(tab);

        Console.WriteLine(answer);
    }

    //Méthode permettant de trier le tableau
    public static int tri(int[] tab)
    {
        bool yaEuUneInversion = false;
        int intervalle = 0;
        do
        {
            yaEuUneInversion = false;


            for (int i = 0; i < tab.Length - 1; i++)
            {
                if (i == 0) intervalle = valeurAbsolue(tab[i], tab[i + 1]);

                if (tab[i] > tab[i + 1])
                {
                    int temp = tab[i];
                    tab[i] = tab[i + 1];
                    tab[i + 1] = temp;
                    yaEuUneInversion = true;
                }

                if (valeurAbsolue(tab[i], tab[i + 1]) < intervalle)
                {
                    intervalle = valeurAbsolue(tab[i], tab[i + 1]);
                }
            }
        } while (yaEuUneInversion);

        return intervalle;
    }

    //Recherche de l'intervalle le plus court entre 2 valeurs
    public static int rechercheIntervalleLePlusCourt(int[] tab)
    {
        int intervalle = 0;

        for (int i = 0; i < tab.Length - 1; i++)
        {
            if (i == 0)
            {
                intervalle = valeurAbsolue(tab[i], tab[i + 1]);
            }

            else if (valeurAbsolue(tab[i], tab[i + 1]) < intervalle)
            {
                intervalle = valeurAbsolue(tab[i], tab[i + 1]);
            }
        }

        return intervalle;

    }

    static public void TriParInsertion(int[] tableauATrier)
    {
        int indiceDuTableau = 1, indiceQuiParcourtLeTableau, valeurTemporaire;

        for (indiceDuTableau = 1; indiceDuTableau < tableauATrier.Length; indiceDuTableau++)
        {
            valeurTemporaire = tableauATrier[indiceDuTableau];
            indiceQuiParcourtLeTableau = indiceDuTableau - 1;
            while (indiceQuiParcourtLeTableau >= 0 && valeurTemporaire < tableauATrier[indiceQuiParcourtLeTableau])
            {
                tableauATrier[indiceQuiParcourtLeTableau + 1] = tableauATrier[indiceQuiParcourtLeTableau];
                indiceQuiParcourtLeTableau--;
            }
            tableauATrier[indiceQuiParcourtLeTableau + 1] = valeurTemporaire;
        }
    }

    static public int valeurAbsolue(int a, int b)
    {
        int abs = 0;
        if (a - b < 0)
        {
            abs = b - a;
        }

        else
        {
            abs = a - b;
        }

        return abs;
    }

    public static int rechercheIntervalle(int[] tab)
    {
        int intervalle = 0;
        for (int i = 0; i < tab.Length - 1; i++)
        {
            for (int j = i + 1; j < tab.Length; j++)
            {
                if (i == 0 && j == 1) intervalle = valeurAbsolue(tab[i], tab[j]);

                else if (valeurAbsolue(tab[i], tab[j]) < intervalle)
                {
                    intervalle = valeurAbsolue(tab[i], tab[j]);
                }

            }
            if (intervalle == 0) break;
        }

        return intervalle;
    }

    static public int rechercheOptimisee(int[] tab)
    {
        int intervalle = 0;
        int index = 0;
        int indexFinal = 0;
        int[] tabFinal = new int[2];
        int valeurMax = 0;
        for (int i = 0; i < tab.Length - 1; i++)
        {
            index = 0;
            for (int j = 0; j < tab.Length; j++)
            {
                valeurMax = 0;
                if (tab[j] > valeurMax)
                {
                    valeurMax = tab[j];
                    index = j;
                }
            }
            tab[index] = -1;
        }

        for (int i = 0; i < tab.Length; i++)
        {
            if (tab[i] != -1)
            {
                tabFinal[indexFinal] = tab[i];
                indexFinal++;
            }
        }

        return valeurAbsolue(tabFinal[0], tabFinal[1]);

    }
}
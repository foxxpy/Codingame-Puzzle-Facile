using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]); // the X position of the light of power
        int lightY = int.Parse(inputs[1]); // the Y position of the light of power
        int initialTx = int.Parse(inputs[2]); // Thor's starting X position
        int initialTy = int.Parse(inputs[3]); // Thor's starting Y position

        // game loop
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.

            string move = "";

            /* D�placement de Thor sur l'axe des Y*/
            if (initialTy > lightY)
            {
                move += "N";
                initialTy++;
            }


            else if (initialTy < lightY)
            {
                move += "S";
                initialTy += 1;
            }

            /*D�placement de Thor sur l'axe des X : W, E ou rien*/
            if (initialTx > lightX)
            {
                move += "W";
                initialTx -= 1;
            }


            else if (initialTx < lightX)
            {
                move = move + "E";
                initialTx += 1;
            }
            Console.WriteLine(move);
        }
    }
}
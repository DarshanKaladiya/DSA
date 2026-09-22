using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{

			//1-D
			// int [5] a = {1, 2, 3, 4, 5};

			// for (int i = 0; i < 5; i++)
			// {
			// 	Console.WriteLine(a[i]);
			// }

//----------------------------------------------------------------------------

			//2-D
			// int [,] a = {{1, 2, 3},{4, 5, 6}};

			// for (int i = 0; i < 2; i++)
            // {
            //     for (int j = 0; j < 3; j++)
            //     {
            //         Console.WriteLine(a[i, j]);
            //     }
            // }

//----------------------------------------------------------------------------

			//3-D
			// int[,,] a = new int[3, 3, 3];

			// int value = 1;

			// for (int i = 0; i < 3; i++)
			// {
			// 	for (int j = 0; j < 3; j++)
			// 	{
			// 		for (int k = 0; k < 3; k++)
			// 		{
			// 			a[i, j, k] = value++;

			// 			Console.WriteLine(a[i, j, k]);
			// 		}
			// 	}
			// }

//----------------------------------------------------------------------------

			//4-D
			int[,,,] a = new int[3, 3, 3, 3];

			int value = 1;

			for (int i = 0; i < 3; i++)
			{
				for (int j = 0; j < 3; j++)
				{
					for (int k = 0; k < 3; k++)
					{
						for (int l = 0; l < 3; l++)
						{
							a[i, j, k, l] = value++;

							Console.WriteLine(a[i, j, k, l]);
						}
					}
				}
			}



		}
	}
}
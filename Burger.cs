//Problem Code: BURGERS

using System;

public class Test
{
	public static void Main()
	{
		int t = Convert.ToInt32(Console.ReadLine());
		
		for (int i = 0; i < t; i++) 
        {
            
            var line = Console.ReadLine();
            var data = line.Split(' ');
            var a = int.Parse(data[0]); //first integer
            var b = int.Parse(data[1]);
            
            //int a = Convert.ToInt32(Console.ReadLine());
            //int b = Convert.ToInt32(Console.ReadLine());
            
            if (a<b)
            {
                Console.WriteLine(a);
            }
            else
            {
                Console.WriteLine(b);
            }
        }
	}
}

package umayam_fcfs;
import java.util.*;
public class Umayam_FCFS {
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter no of Process:  ");
		int n = sc.nextInt();
		int Process[] = new int[n];
		int arrivaltime[] = new int[n];
		int bursttime[] = new int[n];
		int ct[] = new int[n];
		int turnaround[] = new int[n];
		int waitingtime[] = new int[n];
		int temp;
		float avgwt=0,avgta=0;
                        
		for(int i = 0; i < n; i++)
		{
			System.out.println("  Enter Process  " + (i+1) + "  Arrival Time: ");
			arrivaltime[i] = sc.nextInt();
			System.out.println("  Enter Process  " + (i+1) + "  Burst Time: ");
			bursttime[i] = sc.nextInt();
			Process[i] = i+1;
		}
		for(int i = 0 ; i <n; i++)
		{
			for(int  j=0;  j < n-(i+1) ; j++)
			{
				if( arrivaltime[j] > arrivaltime[j+1] )
				{
					temp = arrivaltime[j];
					arrivaltime[j] = arrivaltime[j+1];
					arrivaltime[j+1] = temp;
					temp = bursttime[j];
					bursttime[j] = bursttime[j+1];
					bursttime[j+1] = temp;
					temp = Process[j];
					Process[j] = Process[j+1];
					Process[j+1] = temp;
				}
			}
		}
		for(int  i = 0 ; i < n; i++)
		{
			if( i == 0)
			{	
				ct[i] = arrivaltime[i] + bursttime[i];
			}
			else
			{
				if( arrivaltime[i] > ct[i-1])
				{
					ct[i] = arrivaltime[i] + bursttime[i];
				}
				else
					ct[i] = ct[i-1] + bursttime[i];
			}
			turnaround[i] = ct[i] - arrivaltime[i] ;  
			waitingtime[i] = turnaround[i] - bursttime[i] ;  
			avgwt += waitingtime[i] ;  
			avgta += turnaround[i] ;   
		}
                    System.out.println("\n  Process  Arrival   Burst  Turnaround Waiting");
		for(int  i = 0 ; i< n;  i++)
		{
			System.out.println(Process[i] + "       \t" + arrivaltime[i] +"\t" + bursttime[i] + "    \t" + turnaround[i] + "     \t "  + waitingtime[i] ) ;
		}
		sc.close();
		System.out.println("\nAverage Waiting Time: "+ (avgwt/n));
		System.out.println("Average Waiting TIme: "+(avgta/n));
	}
}
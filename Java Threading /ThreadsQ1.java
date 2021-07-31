
public class ThreadsQ1 {
	static class MThreads extends Thread{
		private long result; 
		private long start ; 
		private long end ;
		public MThreads(long start , long end ) {
			this.start = start ; 
			this.end = end ;
			result = 0 ;
		}
		@Override
		public void run() {
			result = CalculateNumbers(start , end); 
		}
		public long getRnd() {
			return result;
		}
		public static long CalculateNumbers(long start , long end) {
				long total = 0 ;
				for(long i = start ; i <= end ; i++)
				total += i ;
				return total ;
			}
	}
		static class SThread extends Thread {
			private long end ;
			private long result ; 
			public SThread(long end ) {
				this.end = end ;
				result = 0 ;
			}
			public void run() {
				for(long i = 1 ; i <= end ; i++)
					result += i ; 
			}
			public long getRnd() {
				return result;
			}
		public static void main(String[] args) throws InterruptedException {
			SThread st1 = new SThread(100000000);
			long start = System.currentTimeMillis();
			st1.start();
			st1.join();
			long end = System.currentTimeMillis();
			long total = st1.getRnd();
			System.out.println(total);
			System.out.println("Execution Time : " + ((end - start))+" ms");
		}
		}

	
	public static void main(String[] args) throws InterruptedException {

		System.out.println("MultiThreads");
		long startTime = System.currentTimeMillis();
		MThreads t1 = new MThreads(1 , 25000000);
		MThreads t2 = new MThreads(25000000 +1 , 50000000);
		MThreads t3 = new MThreads(50000000 +1 , 75000000);
		MThreads t4 = new MThreads(75000000+1 , 100000000);
		t1.start();
		t2.start();
		t3.start();
		t4.start();
		t1.join();
		t2.join();
		t3.join();
		t4.join();
		long endTime = System.currentTimeMillis();
		long total = t1.getRnd() + t2.getRnd()+ t3.getRnd()+ t4.getRnd();
		System.out.println("sum :"+total);
		System.out.println("Execution Time : " + ((endTime - startTime)/1000.0)+" ms");
		
		System.out.println("Single Thread");
		SThread st1 = new SThread(100000000);
		long start = System.currentTimeMillis();
		st1.start();
		st1.join();
		long end = System.currentTimeMillis();
		long total1 = st1.getRnd();
		System.out.println("sum = "+total);
		System.out.println("Execution Time : " + ((end - start)/1000.0)+" ms");
	}
	}




public class InterrupHandling {
	static class Handling1 extends Thread {
		private boolean flag = false;

		@Override
		public void run() {

			for (int i = 1; i <= 5; i++) {
				System.out.println("Approach 1 :Thread : "+ i +" is working");
				if (Thread.currentThread().isInterrupted()) {
					System.out.println("Approach 1 :Thread : "+i+" interupted");
					System.out.println("Approach 1 :Thread : "+i+" stopped execution ");
					break;
				}
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					System.out.println("Approach 1 :Thread : "+i+" interupted");
					System.out.println("Approach 1 :Thread : "+i+" stopped execution ");
				}
				
			}
		}

	}
	static class Handling2 extends Thread{

		@Override
		public void run() {
			for (int i = 1; i <= 5; i++) {
				System.out.println("Approach 2 :Thread : "+ i +" is working");
			
				
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				System.out.println("Approach 2 :Thread : "+i+" interupted");
				System.out.println("Approach 2 :Thread : "+ i +" stopped execution");
				break;
			}
		}}
		
	}


	public static void main(String[] args) throws InterruptedException {
		Handling1 thread1 = new Handling1();
		Handling2 thread2 = new Handling2();

		thread1.start();
		thread1.sleep(50);
		thread1.interrupt();
		thread1.sleep(110);
		thread1.interrupt();
		thread1.join();
		thread2.start();
		thread2.interrupt();
		thread2.join();

	}

	}

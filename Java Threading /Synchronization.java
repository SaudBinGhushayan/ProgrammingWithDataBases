import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Synchronization {
	static class Writer extends Thread {
		private String symbol;
		public String fileName;
		private BufferedWriter write = null;

		public Writer(String fileName, String symbol) {
			this.fileName = fileName;
			this.symbol = symbol;
			try {
				write = new BufferedWriter(new FileWriter(fileName, true));
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		public synchronized void run() {
			try {
				write.append("Thread "+symbol+" started writing\n");
				write.append("Thread "+symbol+" is currently writing\n");
				write.append("Thread "+symbol+" finished writing – Saud BinGhushayan\n");
				
				write.close();
			

		} catch (IOException e) {
			e.printStackTrace();
		}
		}
	}
	
	public static void main(String[] args) {

		String fileName = "sharable.txt";
		Writer Thread1 = new Writer(fileName, "x");
		Writer Thread2 = new Writer(fileName, "y");
		Writer Thread3 = new Writer(fileName, "z");
		
		try {
		Thread1.start();
		Thread1.join();

		Thread2.start();
		Thread2.join();

		Thread3.start();
		Thread3.join();
		
		System.out.println("completed");
	
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
	}

}

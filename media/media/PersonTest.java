//Blake Ruzich btr5np, and rtb7rd Ryan Bannon

import java.util.ArrayList;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;



public class PersonTest 
{

	private Person p1;
	private Book b1,b2,b3;
	
	@Before
	public void setUp() throws Exception
	{
		p1 = new Person("Blake",10);
		b1= new Book("Harry Potter","JK Rowling");
		b2=new Book("Hunger Games","Suzanne Collins");
		b3=new Book("Hunger Games","Suzanne Collins");
		
		
	}
	
	@Test(timeout=100)
	public void testAddBook() 
	{
		assertTrue(p1.addBook(b1));
		ArrayList<Book> readList = p1.getRead();
		assertTrue(readList.contains(b1));
		
		assertTrue(p1.addBook(b2));
		ArrayList<Book> readList1=p1.getRead();
		assertTrue(readList1.contains(b2));
		assertTrue(readList1.contains(b1));
		
		assertFalse(p1.addBook(b3));
		
	}
	
	@Test(timeout=100)
	public void testForgetBook()
	{
		p1.addBook(b1);
		assertTrue(p1.forgetBook(b1));
		assertFalse(p1.forgetBook(b2));
	}
	
	
	
	

	
	

}

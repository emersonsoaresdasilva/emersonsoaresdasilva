import javax.swing.JOptionPane;
public class Tabuada {
	public static void main(String[] args) {
	     int X=0;
	     //int res=0;
	     X = Integer.parseInt(JOptionPane.showInputDialog("Digite um número X"));
	 for(int cont=0;cont<=10;cont++){
		 JOptionPane.showMessageDialog(null,X+" x "+cont+" = "+X*cont);
	 }
	}
}
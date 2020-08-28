import javax.swing.JOptionPane;

public class LacoFor {

	public static void main(String[] args) {
       //PROGRAMA TABUADA
	   double num1=Double.parseDouble(JOptionPane.showInputDialog("Digite um número"));
	   JOptionPane.showMessageDialog(null, "Você selecionou a tabuada do "+num1);
	   for(int cont=0;cont<=10;cont++){
		   JOptionPane.showMessageDialog(null, num1+" X "+cont+" = "+num1*cont);
	   }
	}

}

import javax.swing.JOptionPane;

public class GerarPares {

	public static void main(String[] args) {
		int num,res=0,cont;
		num=Integer.parseInt(JOptionPane.showInputDialog("Digite o número para gerar os pares"));
		if(num%2==1){
			res=num-1;			
		}
		for(cont=0;cont<=res;cont=cont+2){
			JOptionPane.showMessageDialog(null, cont);
		}
	}

}
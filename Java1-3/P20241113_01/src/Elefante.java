
public class Elefante extends Mammifero implements Must, Req, Comparable<Elefante> {

	private Double peso;
	
	
	public Double getPeso() {
		return peso;
	}

	public void setPeso(Double peso) {
		this.peso = peso;
	}


	@Override
	public String toString() {
		return "Elefante [peso=" + peso + ", getPeso()=" + getPeso() + ", GetClassName()=" + GetClassName()
				+ ", GetVersion()=" + GetVersion() + ", GetSerial()=" + GetSerial() + ", Verso()=" + Verso() + "]";
	}
	
	
	@Override
	public Integer getFreqResp() {
		// TODO Auto-generated method stub
		return super.getFreqResp();
	}

	@Override
	public void setFreqResp(Integer freqResp) {
		// TODO Auto-generated method stub
		super.setFreqResp(freqResp);
	}

	@Override
	public Integer getFreqCardio() {
		// TODO Auto-generated method stub
		return super.getFreqCardio();
	}

	@Override
	public void setFreqCardio(Integer freqCardio) {
		// TODO Auto-generated method stub
		super.setFreqCardio(freqCardio);
	}

	public Elefante(Integer freqResp, Integer freqCardio, Double peso) {
		super(freqResp, freqCardio);
		this.peso = peso;
	}
	
	

	@Override
	public int compareTo(Elefante o) {
		return peso.compareTo(o.peso);
	}

	@Override
	public String GetClassName() {
		return "Elefante";
	}

	@Override
	public String GetVersion() {
		return "1.0";
	}

	@Override
	public String GetSerial() {
		return "TJ89";
	}

	@Override
	public String Verso() {
		// TODO Auto-generated method stub
		return "Barrito";
	}
	
	
}

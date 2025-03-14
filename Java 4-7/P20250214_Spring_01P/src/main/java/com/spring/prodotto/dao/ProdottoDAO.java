package com.spring.prodotto.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;
import com.spring.prodotto.entity.Prodotto;

@Repository
public class ProdottoDAO {

	private final Map<Integer, Prodotto> prodotti = new HashMap<>();
	

	public boolean salva(Prodotto prodotto) {
		if(prodotti.containsKey(prodotto.getId()))
			return false;
		
		prodotti.put(prodotto.getId(), prodotto);
		return true;
	}

	
}

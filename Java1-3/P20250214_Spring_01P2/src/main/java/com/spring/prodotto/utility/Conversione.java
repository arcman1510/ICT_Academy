package com.spring.prodotto.utility;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

import com.spring.prodotto.SpringProdottoApplication;
import com.spring.prodotto.dto.ProdottoDTO;
import com.spring.prodotto.dto.ProdottoNoIdDTO;
import com.spring.prodotto.dto.ReportDTO;

public class Conversione {
	public static SpringProdottoApplication convertiDaDTO(ProdottoDTO dto) {
		return new ProdottoDTO(0, dto.getMarca(), dto.getModello(), dto.getDescrizione(), dto.getPrezzoConsigliato(),
				dto.getPrezzoMassimo(), dto.getQuantita(), dto.getCategoria());
	}

	public static ProdottoDTO convertiInDTO(SpringProdottoApplication prodotto) {
		return new ProdottoDTO(prodotto.getMarca(), prodotto.getModello(), prodotto.getDescrizione(),
				prodotto.getPrezzoConsigliato(), prodotto.getPrezzoMassimo(), prodotto.getQuantita(),
				prodotto.getCategoria());
	}

	public static ProdottoNoIdDTO convertiNoIdDTO(SpringProdottoApplication prodotto) {
		return new ProdottoNoIdDTO(prodotto.getMarca(), prodotto.getModello(), prodotto.getDescrizione(),
				prodotto.getPrezzoConsigliato(), prodotto.getPrezzoMassimo(), prodotto.getQuantita(),
				prodotto.getCategoria());
	}

	public static ReportDTO generaReportDaProdotti(Collection<SpringProdottoApplication> prodotti) {
		List<String> descrizioni = prodotti.stream().map(SpringProdottoApplication::getDescrizione).collect(Collectors.toList());
		int pezziTotali = prodotti.stream().mapToInt(SpringProdottoApplication::getQuantita).sum();
		List<String> nonDisponibili = prodotti.stream().filter(p -> p.getQuantita() == 0).map(SpringProdottoApplication::getModello)
				.collect(Collectors.toList());
		double mediaPrezzi = prodotti.stream().mapToDouble(SpringProdottoApplication::getPrezzoConsigliato).average().orElse(0);

		return new ReportDTO(descrizioni, pezziTotali, nonDisponibili.size(), mediaPrezzi, nonDisponibili);
	}
}
